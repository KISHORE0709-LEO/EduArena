#!/usr/bin/env python3
"""
Clean Manim-based animation server
No OpenAI dependencies - pure Manim generation
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import traceback

# Import our Manim generator
from simple_educational_generator import EducationalVideoGenerator

app = FastAPI(title="EduArena Manim Animation Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure media directory exists
os.makedirs("media", exist_ok=True)
app.mount("/media", StaticFiles(directory="media"), name="media")

# Initialize Educational Video generator
print("Initializing Educational Video generator...")
edu_gen = EducationalVideoGenerator()
executor = ThreadPoolExecutor(max_workers=1)  # Single worker to avoid conflicts

class AnimationRequest(BaseModel):
    prompt: str

# Store animation status
animation_status = {}

@app.post("/generate-animation")
async def generate_animation(request: AnimationRequest):
    animation_id = str(uuid.uuid4())
    
    print(f"Received animation request: {request.prompt}")
    
    # Set initial status
    animation_status[animation_id] = {
        "status": "processing",
        "video_url": None,
        "prompt": request.prompt
    }
    
    # Start animation generation in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(
        executor, 
        generate_educational_video, 
        request.prompt, 
        animation_id
    )
    
    return {
        "id": animation_id,
        "status": "processing",
        "message": "Animation generation started"
    }

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

@app.post("/fix-status/{animation_id}")
async def fix_animation_status(animation_id: str):
    """Manually fix status for stuck animations"""
    
    # Check which files exist
    animation_file = os.path.join("media", f"{animation_id}_animation.mp4")
    explanation_file = os.path.join("media", f"{animation_id}_explanation.mp4")
    final_file = os.path.join("media", f"{animation_id}_final.mp4")
    
    animation_exists = os.path.exists(animation_file)
    explanation_exists = os.path.exists(explanation_file)
    final_exists = os.path.exists(final_file)
    
    if animation_exists or explanation_exists or final_exists:
        # Update status to completed
        main_video = None
        if final_exists:
            main_video = f"/video/{animation_id}_final.mp4"
        elif animation_exists:
            main_video = f"/video/{animation_id}_animation.mp4"
        elif explanation_exists:
            main_video = f"/video/{animation_id}_explanation.mp4"
        
        animation_status[animation_id] = {
            "status": "completed",
            "video_url": main_video,
            "animation_url": f"/video/{animation_id}_animation.mp4" if animation_exists else None,
            "explanation_url": f"/video/{animation_id}_explanation.mp4" if explanation_exists else None,
            "instructions": {
                "concept": "Educational Animation",
                "description": "Generated educational content",
                "educational_points": [
                    "Visual demonstration",
                    "Interactive learning",
                    "Concept visualization"
                ]
            },
            "prompt": animation_status.get(animation_id, {}).get("prompt", "Unknown")
        }
        
        return {
            "message": "Status fixed",
            "files_found": {
                "animation": animation_exists,
                "explanation": explanation_exists,
                "final": final_exists
            }
        }
    else:
        raise HTTPException(status_code=404, detail="No video files found for this animation ID")

def generate_educational_video(prompt: str, animation_id: str):
    """Background task to generate complete educational video"""
    try:
        print(f"Starting educational video generation for: {prompt}")
        result = edu_gen.generate_complete_educational_video(prompt, animation_id)
        
        if result and result["status"] == "completed":
            print(f"Educational video generated successfully")
            
            # Check which files actually exist
            final_video = f"/video/{animation_id}_final.mp4" if os.path.exists(os.path.join("media", f"{animation_id}_final.mp4")) else None
            animation_video = f"/video/{animation_id}_animation.mp4" if os.path.exists(os.path.join("media", f"{animation_id}_animation.mp4")) else None
            explanation_video = f"/video/{animation_id}_explanation.mp4" if os.path.exists(os.path.join("media", f"{animation_id}_explanation.mp4")) else None
            
            # Use animation as main video if final doesn't exist
            main_video = final_video or animation_video
            
            # Update status with comprehensive result
            animation_status[animation_id] = {
                "status": "completed",
                "video_url": main_video,
                "animation_url": animation_video,
                "explanation_url": explanation_video,
                "instructions": result["instructions"],
                "prompt": prompt
            }
        else:
            print(f"Failed to generate educational video for: {prompt}")
            # Check if at least animation file exists
            animation_video = f"/video/{animation_id}_animation.mp4" if os.path.exists(os.path.join("media", f"{animation_id}_animation.mp4")) else None
            
            if animation_video:
                # Partial success - at least animation was created
                animation_status[animation_id] = {
                    "status": "completed",
                    "video_url": animation_video,
                    "animation_url": animation_video,
                    "explanation_url": None,
                    "instructions": {"concept": "Animation Generated", "educational_points": ["Visual demonstration created"]},
                    "prompt": prompt
                }
            else:
                animation_status[animation_id] = {
                    "status": "failed",
                    "video_url": None,
                    "prompt": prompt,
                    "error": "Failed to generate educational video"
                }
    except Exception as e:
        print(f"Error generating educational video: {str(e)}")
        print(traceback.format_exc())
        animation_status[animation_id] = {
            "status": "failed",
            "video_url": None,
            "prompt": prompt,
            "error": str(e)
        }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "manim-animation-server"}

@app.get("/")
async def root():
    return {"message": "EduArena Educational Video Server", "status": "running", "features": ["Structured Instructions", "Visual Animations", "Educational Explanations"]}

if __name__ == "__main__":
    import uvicorn
    print("Starting EduArena Manim Animation Server...")
    print("Server will be available at: http://localhost:8008")
    print("Health check: http://localhost:8008/health")
    uvicorn.run(app, host="0.0.0.0", port=8008, log_level="info")