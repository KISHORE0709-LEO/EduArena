import os
import sys
import subprocess
import shutil
import uuid
import asyncio
from concurrent.futures import ThreadPoolExecutor

# SET FFMPEG PATH FIRST
backend_dir = r"D:\Kishore\New_project\EduArena\backend"
ffmpeg_path = r"D:\Kishore\New_project\EduArena\backend\ffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"
os.environ['FFMPEG_BINARY'] = ffmpeg_path
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path

# IMPORT MANIM AFTER SETTING PATH
import manim
manim.config.ffmpeg_executable = ffmpeg_path
manim.config.media_dir = os.path.join(backend_dir, "media")
manim.config.disable_caching = True

from manim import *
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
        class QuickScene(Scene):
            def construct(self):
                text = Text(prompt[:15], font_size=48)
                self.add(text)
                self.wait(1)
        
        scene = QuickScene()
        scene.render()
        
        # Find video file
        for root, dirs, files in os.walk(os.path.join(backend_dir, "media")):
            for file in files:
                if file.endswith('.mp4') and 'QuickScene' in file:
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
    uvicorn.run(app, host="0.0.0.0", port=4000)