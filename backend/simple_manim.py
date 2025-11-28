from manim import *

class BernoulliScene(Scene):
    def construct(self):
        title = Text("Bernoulli's Principle", font_size=36, color=BLUE).to_edge(UP)
        
        # Simple airfoil
        airfoil = Ellipse(width=4, height=1, color=BLUE)
        airfoil.set_fill(BLUE, opacity=0.3)
        
        # Flow lines
        flow_lines = VGroup()
        for i in range(5):
            line = Arrow(start=LEFT * 4, end=RIGHT * 4, color=RED if i < 2 else GREEN)
            line.shift(UP * (i - 2) * 0.8)
            flow_lines.add(line)
        
        # Labels
        top_text = Text("Higher Velocity, Lower Pressure", font_size=16, color=RED)
        top_text.next_to(airfoil, UP, buff=1)
        
        bottom_text = Text("Lower Velocity, Higher Pressure", font_size=16, color=GREEN)
        bottom_text.next_to(airfoil, DOWN, buff=1)
        
        # Lift force
        lift_arrow = Arrow(start=ORIGIN, end=UP * 2, color=YELLOW, stroke_width=8)
        lift_label = Text("LIFT", font_size=24, color=YELLOW).next_to(lift_arrow, RIGHT)
        
        # Simple text equation (no LaTeX)
        equation = Text("P + (1/2)ρv² = constant", font_size=24, color=WHITE)
        equation.to_edge(DOWN)
        
        # Animate
        self.play(Write(title))
        self.play(Create(airfoil))
        self.play(Create(flow_lines), run_time=3)
        self.play(Write(top_text), Write(bottom_text), run_time=2)
        self.play(Create(lift_arrow), Write(lift_label))
        self.play(Write(equation), run_time=2)
        self.wait(3)

class MatrixScene(Scene):
    def construct(self):
        title = Text("4x4 Matrix Exponentiation", font_size=36, color=BLUE).to_edge(UP)
        
        # Simple matrix representation
        matrix_text = Text("4x4 Matrix A", font_size=24, color=WHITE)
        matrix_box = Rectangle(width=3, height=3, color=BLUE)
        matrix_group = VGroup(matrix_box, matrix_text)
        
        # Exponentiation
        exp_text = Text("A^n = A × A × ... × A", font_size=20, color=YELLOW)
        exp_text.next_to(matrix_group, DOWN, buff=1)
        
        # Applications
        apps = Text("Applications: Graph algorithms, Dynamic programming", font_size=16, color=GREEN)
        apps.to_edge(DOWN)
        
        # Animate
        self.play(Write(title))
        self.play(Create(matrix_box), Write(matrix_text))
        self.play(Write(exp_text))
        self.play(Write(apps))
        self.wait(3)