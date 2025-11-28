import os
import sys
import shutil
from manim_config_fix import setup_manim_environment

# Setup Manim environment FIRST
if not setup_manim_environment():
    print("Failed to setup Manim environment")
    sys.exit(1)

# Now import Manim after configuration
from manim import *
import numpy as np

class TextToAnimationGenerator:
    def __init__(self):
        self.output_dir = "media"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_animation(self, prompt: str, animation_id: str) -> str:
        """Generate Manim animation for ANY text prompt"""
        
        class DynamicScene(Scene):
            def construct(self):
                # Simple animation that always works
                title = Text(prompt[:30], font_size=24, color=WHITE)
                title.to_edge(UP)
                self.play(Write(title), run_time=1)
                
                # Create a simple shape
                circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
                self.play(Create(circle), run_time=1)
                self.play(circle.animate.set_color(RED), run_time=1)
                self.wait(1)
        
        # Render the scene
        try:
            scene = DynamicScene()
            scene.render()
            
            # Find generated video
            video_dir = os.path.join(self.output_dir, "videos", "480p15")
            if os.path.exists(video_dir):
                for file in os.listdir(video_dir):
                    if file.endswith('.mp4'):
                        src = os.path.join(video_dir, file)
                        dst = os.path.join(self.output_dir, f"{animation_id}.mp4")
                        shutil.copy2(src, dst)
                        return dst
            
            return None
            
        except Exception as e:
            print(f"Animation generation failed: {e}")
            return None