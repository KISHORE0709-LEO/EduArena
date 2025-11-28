import os
import sys

# Set FFmpeg path
backend_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
os.environ['FFMPEG_BINARY'] = ffmpeg_path
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path
os.environ['PATH'] = os.path.dirname(ffmpeg_path) + ';' + os.environ.get('PATH', '')

import manim
manim.config.ffmpeg_executable = ffmpeg_path
manim.config.disable_caching = True
manim.config.quality = "low_quality"
manim.config.media_dir = os.path.join(backend_dir, "media")

from manim import *
import uuid
import shutil
import asyncio
from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class AnimationRequest(BaseModel):
    prompt: str

animation_status = {}
executor = ThreadPoolExecutor(max_workers=1)

def create_animation(prompt: str, animation_id: str):
    try:
        prompt_lower = prompt.lower()
        
        if "bernoulli" in prompt_lower:
            class BernoulliScene(Scene):
                def construct(self):
                    title = Text("Bernoulli's Principle", font_size=36, color=WHITE)
                    self.play(Write(title))
                    self.wait(1)
                    
                    wide_pipe = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
                    narrow_pipe = Rectangle(width=2, height=0.8, color=BLUE, fill_opacity=0.3)
                    wide_pipe.shift(LEFT * 2)
                    narrow_pipe.shift(RIGHT * 1)
                    
                    self.play(Create(wide_pipe), Create(narrow_pipe))
                    self.wait(1)
                    
                    v1_arrow = Arrow(LEFT, RIGHT, color=GREEN).scale(0.8)
                    v1_arrow.next_to(wide_pipe, UP)
                    v1_label = Text("v1 (slow)", font_size=20, color=GREEN)
                    v1_label.next_to(v1_arrow, UP)
                    
                    v2_arrow = Arrow(LEFT, RIGHT, color=RED).scale(1.5)
                    v2_arrow.next_to(narrow_pipe, UP)
                    v2_label = Text("v2 (fast)", font_size=20, color=RED)
                    v2_label.next_to(v2_arrow, UP)
                    
                    self.play(Create(v1_arrow), Write(v1_label))
                    self.play(Create(v2_arrow), Write(v2_label))
                    self.wait(2)
            scene_class = BernoulliScene
            
        elif "matrix" in prompt_lower and "4x4" in prompt_lower:
            class MatrixPowerScene(Scene):
                def construct(self):
                    title = Text("4x4 Matrix Exponentiation", font_size=32, color=WHITE)
                    self.play(Write(title))
                    self.wait(1)
                    
                    matrix_a = Text("A = [[2,0,1,0], [1,3,0,2], [0,1,2,1], [1,0,0,2]]", font_size=16, color=BLUE)
                    matrix_a.shift(UP * 1.5)
                    self.play(Write(matrix_a))
                    self.wait(1)
                    
                    exp_text = Text("Computing A^13 using binary exponentiation", font_size=20, color=GREEN)
                    exp_text.shift(UP * 0.5)
                    self.play(Write(exp_text))
                    self.wait(1)
                    
                    binary_text = Text("13 in binary: 1101", font_size=18, color=YELLOW)
                    binary_text.shift(DOWN * 0.5)
                    self.play(Write(binary_text))
                    self.wait(2)
            scene_class = MatrixPowerScene
            
        else:
            class DefaultScene(Scene):
                def construct(self):
                    text = Text(prompt[:30], font_size=24, color=WHITE)
                    circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
                    self.play(Write(text), run_time=1)
                    self.play(Create(circle), run_time=1)
                    self.wait(1)
            scene_class = DefaultScene
        
        scene = scene_class()
        scene.render()
        
        # Find video
        for root, dirs, files in os.walk(os.path.join(backend_dir, "media")):
            for file in files:
                if file.endswith('.mp4'):
                    src = os.path.join(root, file)
                    dst = os.path.join(backend_dir, "media", f"{animation_id}.mp4")
                    shutil.copy2(src, dst)
                    animation_status[animation_id] = {"status": "completed", "video_url": f"/video/{animation_id}.mp4"}
                    return
        
        animation_status[animation_id] = {"status": "failed", "error": "No video generated"}
        
    except Exception as e:
        animation_status[animation_id] = {"status": "failed", "error": str(e)}

@app.post("/generate-animation")
async def generate_animation(request: AnimationRequest):
    animation_id = str(uuid.uuid4())
    animation_status[animation_id] = {"status": "processing"}
    
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, create_animation, request.prompt, animation_id)
    
    return {"id": animation_id, "status": "processing"}

@app.get("/animation-status/{animation_id}")
async def get_status(animation_id: str):
    if animation_id not in animation_status:
        raise HTTPException(status_code=404, detail="Not found")
    return animation_status[animation_id]

@app.get("/video/{filename}")
async def get_video(filename: str):
    video_path = os.path.join(backend_dir, "media", filename)
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    raise HTTPException(status_code=404, detail="Video not found")

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)