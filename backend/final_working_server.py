from manim_config_fix import setup_manim_environment

# Setup environment FIRST
if not setup_manim_environment():
    print("FAILED TO SETUP MANIM")
    exit(1)

# Now import everything else
from manim import *
import os
import sys
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

def create_animation_video(prompt: str, animation_id: str):
    try:
        class SimpleAnimationScene(Scene):
            def construct(self):
                text = Text(prompt[:20], font_size=36, color=WHITE)
                circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
                self.play(Write(text), run_time=1)
                self.play(Create(circle), run_time=1)
                self.wait(1)
        
        # Render scene
        scene = SimpleAnimationScene()
        scene.render()
        
        # Find the generated video
        backend_dir = os.path.dirname(os.path.abspath(__file__))
        media_dir = os.path.join(backend_dir, "media")
        
        video_file = None
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                if file.endswith('.mp4') and 'SimpleAnimationScene' in file:
                    video_file = os.path.join(root, file)
                    break
            if video_file:
                break
        
        if video_file:
            # Copy to final location
            final_path = os.path.join(media_dir, f"{animation_id}.mp4")
            shutil.copy2(video_file, final_path)
            animation_status[animation_id] = {
                "status": "completed",
                "video_url": f"/video/{animation_id}.mp4",
                "prompt": prompt
            }
        else:
            animation_status[animation_id] = {
                "status": "failed",
                "error": "Video file not found after rendering",
                "prompt": prompt
            }
            
    except Exception as e:
        animation_status[animation_id] = {
            "status": "failed", 
            "error": str(e),
            "prompt": prompt
        }

@app.post("/generate-animation")
async def generate_animation(request: AnimationRequest):
    animation_id = str(uuid.uuid4())
    animation_status[animation_id] = {"status": "processing", "prompt": request.prompt}
    
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, create_animation_video, request.prompt, animation_id)
    
    return {"id": animation_id, "status": "processing"}

@app.get("/animation-status/{animation_id}")
async def get_animation_status(animation_id: str):
    if animation_id not in animation_status:
        raise HTTPException(status_code=404, detail="Animation not found")
    return animation_status[animation_id]

@app.get("/video/{filename}")
async def get_video(filename: str):
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(backend_dir, "media", filename)
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    raise HTTPException(status_code=404, detail="Video not found")

@app.get("/health")
async def health():
    return {"status": "healthy", "message": "EduArena backend is running"}

if __name__ == "__main__":
    import uvicorn
    print("Starting EduArena backend server...")
    uvicorn.run(app, host="0.0.0.0", port=8080)