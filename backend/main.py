from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import uuid
from langgraph_workflow import create_animation_workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("media", exist_ok=True)
app.mount("/media", StaticFiles(directory="media"), name="media")

active_workflows = {}

class AnimationRequest(BaseModel):
    prompt: str

class AnimationResponse(BaseModel):
    id: str
    scenes: list
    video_url: str = None
    status: str

@app.post("/generate-animation", response_model=AnimationResponse)
async def generate_animation_endpoint(request: AnimationRequest):
    animation_id = str(uuid.uuid4())
    
    try:
        # Execute existing LangGraph workflow
        result = create_animation_workflow(request.prompt)
        active_workflows[animation_id] = result
        
        # Extract data from workflow result
        scenes = result.get("scenes", [])
        video_url = f"/media/{os.path.basename(result['video_path'])}" if result.get("video_path") else None
        status = result.get("status", "failed")
        
        response = AnimationResponse(
            id=animation_id,
            scenes=scenes,
            video_url=video_url,
            status=status
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/animation/{animation_id}")
async def get_animation_status(animation_id: str):
    if animation_id not in active_workflows:
        raise HTTPException(status_code=404, detail="Animation not found")
    
    result = active_workflows[animation_id]
    
    scenes = result.get("scenes", [])
    video_url = f"/media/{os.path.basename(result['video_path'])}" if result.get("video_path") else None
    status = result.get("status", "failed")
    
    return {
        "id": animation_id,
        "status": status,
        "scenes": scenes,
        "video_url": video_url
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)