import os
import sys

# CRITICAL: Set FFmpeg path BEFORE any imports
backend_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')

# Try alternative path if first doesn't exist
if not os.path.exists(ffmpeg_path):
    ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-master-latest-win64-gpl', 'bin', 'ffmpeg.exe')

if not os.path.exists(ffmpeg_path):
    raise FileNotFoundError(f"FFmpeg not found at {ffmpeg_path}")

os.environ['FFMPEG_BINARY'] = ffmpeg_path
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path
os.environ['PATH'] = os.path.dirname(ffmpeg_path) + ';' + os.environ.get('PATH', '')
print(f"Using FFmpeg: {ffmpeg_path}")

import manim
manim.config.ffmpeg_executable = ffmpeg_path
manim.config.disable_caching = True
manim.config.quality = "low_quality"
manim.config.media_dir = os.path.join(backend_dir, "media")
manim.config.video_dir = os.path.join(backend_dir, "media", "videos")
manim.config.partial_movie_dir = os.path.join(backend_dir, "temp_manim", "partial")
os.makedirs(manim.config.video_dir, exist_ok=True)
os.makedirs(manim.config.partial_movie_dir, exist_ok=True)

from manim import *
import shutil

class TextToAnimationGenerator:
    def __init__(self):
        self.output_dir = "media"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_animation(self, prompt: str, animation_id: str) -> str:
        # Check for specific educational scenes
        prompt_lower = prompt.lower()
        
        if "bernoulli" in prompt_lower:
            from bernoulli_fixed import BernoulliScene
            scene_class = BernoulliScene
        elif "matrix" in prompt_lower and "4x4" in prompt_lower:
            from matrix_fixed import MatrixPowerScene
            scene_class = MatrixPowerScene
        else:
            # Default dynamic scene
            prompt_text = prompt[:30] if len(prompt) > 30 else prompt
            
            class DynamicScene(Scene):
                def construct(scene_self):
                    try:
                        text = Text(prompt_text, font_size=24, color=WHITE)
                        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
                        scene_self.play(Write(text), run_time=1)
                        scene_self.play(Create(circle), run_time=1)
                        scene_self.wait(1)
                    except Exception as e:
                        print(f"Scene construction error: {e}")
                        fallback_text = Text("Animation", font_size=36, color=WHITE)
                        scene_self.add(fallback_text)
                        scene_self.wait(2)
            
            scene_class = DynamicScene
        
        try:
            scene = scene_class()
            scene.render()
            
            # Find and copy video - check multiple possible locations
            possible_dirs = [
                os.path.join(self.output_dir, "videos", "480p15"),
                os.path.join(self.output_dir, "videos"),
                self.output_dir
            ]
            
            for video_dir in possible_dirs:
                if os.path.exists(video_dir):
                    mp4_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
                    if mp4_files:
                        # Get the most recently created MP4 file
                        latest_file = max(mp4_files, key=lambda f: os.path.getctime(os.path.join(video_dir, f)))
                        src = os.path.join(video_dir, latest_file)
                        dst = os.path.join(self.output_dir, f"{animation_id}.mp4")
                        shutil.copy2(src, dst)
                        return dst
            
            # If no video found, list all files in media directory
            print(f"No video found. Contents of {self.output_dir}:")
            for root, dirs, files in os.walk(self.output_dir):
                for file in files:
                    print(f"  {os.path.join(root, file)}")
            
            return None
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            return None