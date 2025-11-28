from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from working_generator import TextToAnimationGenerator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/media", StaticFiles(directory="media"), name="media")

manim_gen = TextToAnimationGenerator()
executor = ThreadPoolExecutor(max_workers=1)

class AnimationRequest(BaseModel):
    prompt: str

animation_status = {}

@app.post("/generate-animation")
async def generate_animation(request: AnimationRequest):
    animation_id = str(uuid.uuid4())
    animation_status[animation_id] = {"status": "processing", "video_url": None, "prompt": request.prompt}
    
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, generate_manim_animation, request.prompt, animation_id)
    
    return {"id": animation_id, "status": "processing"}

@app.get("/animation-status/{animation_id}")
async def get_animation_status(animation_id: str):
    if animation_id not in animation_status:
        raise HTTPException(status_code=404, detail="Animation not found")
    return animation_status[animation_id]

@app.get("/video/{filename}")
async def get_video(filename: str):
    video_path = os.path.join("media", filename)
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    raise HTTPException(status_code=404, detail="Video not found")

def generate_manim_animation(prompt: str, animation_id: str):
    try:
        video_path = manim_gen.generate_animation(prompt, animation_id)
        if video_path and os.path.exists(video_path):
            animation_status[animation_id] = {"status": "completed", "video_url": f"/video/{animation_id}.mp4", "prompt": prompt}
        else:
            animation_status[animation_id] = {"status": "failed", "video_url": None, "prompt": prompt, "error": "Failed to generate video"}
    except Exception as e:
        animation_status[animation_id] = {"status": "failed", "video_url": None, "prompt": prompt, "error": str(e)}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)