from typing import TypedDict, List
from langgraph.graph import StateGraph, END
import openai
import os
from dotenv import load_dotenv
import subprocess
import glob

load_dotenv()

class AnimationState(TypedDict):
    prompt: str
    scenes: List[dict]
    code: str
    video_path: str
    status: str

def plan_scenes(state: AnimationState) -> AnimationState:
    """Director: Break prompt into scenes"""
    
    system_prompt = """Break the user's prompt into 2-3 simple animation scenes.
    Return JSON array with title, description, duration for each scene.
    
    Example:
    [
        {"title": "Setup", "description": "Show initial state", "duration": 2},
        {"title": "Action", "description": "Show main animation", "duration": 3}
    ]"""
    
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state["prompt"]}
        ]
    )
    
    import json
    try:
        scenes = json.loads(response.choices[0].message.content)
    except:
        scenes = [{"title": "Animation", "description": state["prompt"], "duration": 5}]
    
    return {**state, "scenes": scenes, "status": "planned"}

def generate_code(state: AnimationState) -> AnimationState:
    """Coder: Generate Manim code"""
    
    scenes_text = "\n".join([f"Scene {i+1}: {s['title']} - {s['description']}" 
                            for i, s in enumerate(state["scenes"])])
    
    system_prompt = f"""Generate Manim Python code for these scenes:
{scenes_text}

Rules:
- Import: from manim import *
- Class inheriting Scene
- Use construct(self) method
- End with self.wait(2)
- Simple shapes and text only
- Working code only

Return ONLY Python code."""

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create animation for: {state['prompt']}"}
        ]
    )
    
    code = response.choices[0].message.content.strip()
    if code.startswith("```python"):
        code = code[9:-3]
    elif code.startswith("```"):
        code = code[3:-3]
    
    return {**state, "code": code, "status": "coded"}

def render_video(state: AnimationState) -> AnimationState:
    """Renderer: Create video from code"""
    
    # Write code to file
    with open("temp_animation.py", "w") as f:
        f.write(state["code"])
    
    # Render with Manim
    try:
        subprocess.run(["python", "-m", "manim", "-pql", "temp_animation.py", "--media_dir", "media"], 
                      check=True, capture_output=True, timeout=60)
        
        # Find video
        videos = glob.glob("media/videos/**/*.mp4", recursive=True)
        video_path = videos[-1] if videos else None
        
        return {**state, "video_path": video_path, "status": "completed"}
    except:
        return {**state, "status": "failed"}

# Build workflow graph
workflow = StateGraph(AnimationState)

workflow.add_node("plan", plan_scenes)
workflow.add_node("code", generate_code)
workflow.add_node("render", render_video)

workflow.add_edge("plan", "code")
workflow.add_edge("code", "render")
workflow.add_edge("render", END)

workflow.set_entry_point("plan")

app = workflow.compile()

def create_animation_workflow(prompt: str) -> AnimationState:
    """Execute complete workflow"""
    initial_state = {
        "prompt": prompt,
        "scenes": [],
        "code": "",
        "video_path": "",
        "status": "starting"
    }
    
    result = app.invoke(initial_state)
    return result