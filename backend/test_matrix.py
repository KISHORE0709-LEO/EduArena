from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from manim import *
import numpy as np

class MatrixPowerScene(Scene):
    def construct(self):
        A = np.array([[2, 1], [1, 2]], dtype=float)
        n = 5
        
        title = Text("Matrix Power A^5", font_size=36)
        self.play(Write(title))
        self.wait(1)
        
        # Show matrix A
        mat_A = Matrix(A)
        mat_A.scale(0.8)
        self.play(Create(mat_A))
        self.wait(1)
        
        # Compute A^n
        result = np.linalg.matrix_power(A.astype(int), n)
        mat_result = Matrix(result)
        mat_result.scale(0.8)
        mat_result.next_to(mat_A, RIGHT, buff=1)
        
        self.play(Create(mat_result))
        self.wait(2)

if __name__ == "__main__":
    scene = MatrixPowerScene()
    scene.render()