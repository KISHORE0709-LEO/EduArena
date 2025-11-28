import os
import sys
import subprocess

# ABSOLUTE PATH FIX
backend_dir = r"D:\Kishore\New_project\EduArena\backend"
ffmpeg_path = r"D:\Kishore\New_project\EduArena\backend\ffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"

# SET ENVIRONMENT
os.environ['FFMPEG_BINARY'] = ffmpeg_path
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path
os.environ['PATH'] = r"D:\Kishore\New_project\EduArena\backend\ffmpeg\ffmpeg-8.0.1-essentials_build\bin" + ';' + os.environ.get('PATH', '')

# IMPORT MANIM
import manim
manim.config.ffmpeg_executable = ffmpeg_path
manim.config.media_dir = os.path.join(backend_dir, "media")
manim.config.disable_caching = True
manim.config.quality = "low_quality"

from manim import *
import shutil
import uuid

class TextToAnimationGenerator:
    def __init__(self):
        self.output_dir = os.path.join(backend_dir, "media")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_animation(self, prompt: str, animation_id: str) -> str:
        class SimpleScene(Scene):
            def construct(self):
                text = Text(prompt[:20], font_size=36, color=WHITE)
                circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.3)
                self.play(Write(text), run_time=1)
                self.play(Create(circle), run_time=1)
                self.play(circle.animate.set_color(RED), run_time=1)
                self.wait(1)
        
        try:
            # Render scene
            scene = SimpleScene()
            scene.render()
            
            # Find the video file
            video_path = None
            for root, dirs, files in os.walk(self.output_dir):
                for file in files:
                    if file.endswith('.mp4') and 'SimpleScene' in file:
                        video_path = os.path.join(root, file)
                        break
                if video_path:
                    break
            
            if video_path:
                # Copy to final location
                final_path = os.path.join(self.output_dir, f"{animation_id}.mp4")
                shutil.copy2(video_path, final_path)
                return final_path
            
            return None
            
        except Exception as e:
            print(f"Animation error: {e}")
            return None

# TEST
if __name__ == "__main__":
    gen = TextToAnimationGenerator()
    result = gen.generate_animation("test animation", "test_final")
    print(f"Result: {result}")