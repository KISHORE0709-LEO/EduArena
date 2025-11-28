from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from manim import *

class SimpleTest(Scene):
    def construct(self):
        text = Text("Hello EduArena", font_size=48, color=WHITE)
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        
        self.play(Write(text), run_time=1)
        self.play(Create(circle), run_time=1)
        self.wait(1)

if __name__ == "__main__":
    scene = SimpleTest()
    scene.render()