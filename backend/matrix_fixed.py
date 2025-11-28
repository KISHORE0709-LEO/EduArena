from manim import *
import numpy as np

class MatrixPowerScene(Scene):
    def construct(self):
        title = Text("4x4 Matrix Exponentiation", font_size=32, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        
        # Show matrix A as text
        matrix_a = Text("A = [[2,0,1,0], [1,3,0,2], [0,1,2,1], [1,0,0,2]]", 
                       font_size=16, color=BLUE)
        matrix_a.shift(UP * 1.5)
        
        self.play(Write(matrix_a))
        self.wait(1)
        
        # Show exponent
        exp_text = Text("Computing A^13 using binary exponentiation", 
                       font_size=20, color=GREEN)
        exp_text.shift(UP * 0.5)
        
        self.play(Write(exp_text))
        self.wait(1)
        
        # Binary representation
        binary_text = Text("13 in binary: 1101", font_size=18, color=YELLOW)
        binary_text.shift(DOWN * 0.5)
        
        self.play(Write(binary_text))
        self.wait(1)
        
        # Algorithm steps
        steps = [
            "Step 1: result = I, power = A",
            "Step 2: bit=1, result = result * power",
            "Step 3: power = power^2",
            "Step 4: Continue for each bit..."
        ]
        
        step_group = VGroup()
        for i, step in enumerate(steps):
            step_text = Text(step, font_size=14, color=WHITE)
            step_text.shift(DOWN * (1.5 + i * 0.4))
            step_group.add(step_text)
        
        self.play(Write(step_group))
        self.wait(2)
        
        # Final result indication
        result_text = Text("Result: 4x4 matrix computed efficiently!", 
                          font_size=18, color=RED)
        result_text.shift(DOWN * 3.5)
        
        self.play(Write(result_text))
        self.wait(2)