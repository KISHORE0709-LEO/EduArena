from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from manim import *
import numpy as np

class MatrixSimpleScene(Scene):
    def construct(self):
        # Simple matrix without LaTeX
        title = Text("Matrix Power Demo", font_size=36)
        self.play(Write(title))
        self.wait(1)
        
        # Show matrix as text (no LaTeX)
        matrix_text = Text("A = [[2, 1], [1, 2]]", font_size=24)
        matrix_text.shift(UP)
        
        result_text = Text("A^3 = [[15, 13], [13, 15]]", font_size=24)
        result_text.shift(DOWN)
        
        self.play(Write(matrix_text))
        self.wait(1)
        self.play(Write(result_text))
        self.wait(2)

if __name__ == "__main__":
    scene = MatrixSimpleScene()
    scene.render()
    print("SUCCESS: Matrix scene rendered without LaTeX")