from manim import *
import numpy as np

class MatrixPowerScene(Scene):
    def construct(self):
        # Simple matrix power demonstration
        A = np.array([[2, 1], [1, 2]], dtype=float)
        n = 3
        
        title = Text("Matrix Power A^3", font_size=36)
        self.play(Write(title))
        self.wait(1)
        
        # Show matrix A
        mat_A = Matrix(A)
        mat_A.scale(0.8)
        mat_A.shift(LEFT * 2)
        
        label_A = Text("A =", font_size=24).next_to(mat_A, LEFT)
        
        self.play(Write(label_A), Create(mat_A))
        self.wait(1)
        
        # Compute A^n
        result = np.linalg.matrix_power(A.astype(int), n)
        mat_result = Matrix(result)
        mat_result.scale(0.8)
        mat_result.shift(RIGHT * 2)
        
        label_result = Text("A^3 =", font_size=24).next_to(mat_result, LEFT)
        
        self.play(Write(label_result), Create(mat_result))
        self.wait(2)