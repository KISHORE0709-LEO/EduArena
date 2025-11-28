from manim import *
import numpy as np

class BernoulliScene(Scene):
    def construct(self):
        # Title with EduArena theme
        title = Text("Bernoulli's Principle", font_size=36, color=BLUE).to_edge(UP)
        
        # Create axes for flow visualization
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_tip": True},
            x_length=10,
            y_length=6
        )
        
        # Airfoil shape
        airfoil = Ellipse(width=4, height=1, color=BLUE)
        airfoil.set_fill(BLUE, opacity=0.3)
        
        # Flow streamlines
        flow_lines = VGroup()
        for i in range(7):
            y_pos = (i - 3) * 0.8
            if abs(y_pos) < 1:  # Near airfoil - faster flow
                line = Arrow(start=LEFT * 4, end=RIGHT * 4, color=RED, stroke_width=3)
            else:  # Away from airfoil - slower flow
                line = Arrow(start=LEFT * 4, end=RIGHT * 4, color=GREEN, stroke_width=5)
            line.shift(UP * y_pos)
            flow_lines.add(line)
        
        # Labels
        velocity_label = Text("Flow Velocity", font_size=20, color=YELLOW).next_to(axes.x_axis, DOWN)
        pressure_label = Text("Pressure Distribution", font_size=20, color=YELLOW).next_to(axes.y_axis, LEFT)
        
        # Bernoulli equation
        equation = MathTex(
            r"P + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}",
            font_size=28,
            color="#00FFFF"
        ).to_edge(DOWN)
        
        # Net lift force
        lift_arrow = Arrow(
            start=ORIGIN,
            end=UP * 2.5,
            color=YELLOW,
            stroke_width=8
        )
        lift_label = Text("LIFT FORCE", font_size=24, color=YELLOW).next_to(lift_arrow, RIGHT)
        
        # Animate everything
        self.play(Write(title))
        self.play(Create(axes), Write(velocity_label), Write(pressure_label))
        self.play(Create(airfoil))
        self.play(Create(flow_lines), run_time=3)
        self.play(Create(lift_arrow), Write(lift_label))
        self.play(Write(equation), run_time=3)
        self.wait(3)

class MatrixScene(Scene):
    def construct(self):
        # Title with EduArena theme
        title = Text("4x4 Matrix Exponentiation", font_size=36, color=BLUE).to_edge(UP)
        
        # Create 4x4 matrix A
        matrix_a = VGroup(
            Text("a  b  c  d", color="#00FFFF"),
            Text("e  f  g  h", color="#00FFFF"),
            Text("i  j  k  l", color="#00FFFF"),
            Text("m  n  o  p", color="#00FFFF")
        ).arrange(DOWN)
        matrix_a.add(SurroundingRectangle(matrix_a, color=BLUE, buff=0.3))
        
        # Exponentiation concept
        exp_label = Text("A^n =", font_size=24, color=YELLOW)
        
        # Multiplication symbols
        times1 = Text("×", font_size=30, color=WHITE)
        times2 = Text("×", font_size=30, color=WHITE)
        times3 = Text("× ...", font_size=30, color=WHITE)
        
        # Multiple matrix copies
        matrix_b = matrix_a.copy()
        matrix_c = matrix_a.copy()
        
        # Arrange multiplication
        multiplication = VGroup(
            exp_label, matrix_a, times1, matrix_b, times2, matrix_c, times3
        ).arrange(RIGHT, buff=0.3)
        
        # Step-by-step calculation
        calc_title = Text("For A^2 = A × A:", font_size=20, color=YELLOW)
        calc1 = Text("Element (1,1) = a×a + b×e + c×i + d×m", font_size=16, color=GREEN)
        calc2 = Text("Element (1,2) = a×b + b×f + c×j + d×n", font_size=16, color=GREEN)
        calc3 = Text("... (16 total calculations)", font_size=16, color=GREEN)
        
        calculations = VGroup(calc_title, calc1, calc2, calc3).arrange(DOWN, aligned_edge=LEFT)
        calculations.next_to(multiplication, DOWN, buff=1)
        
        # Applications
        apps_title = Text("Applications:", font_size=20, color=YELLOW)
        app1 = Text("• Graph path counting", font_size=16, color=ORANGE)
        app2 = Text("• Linear recurrence relations", font_size=16, color=ORANGE)
        app3 = Text("• Dynamic programming", font_size=16, color=ORANGE)
        
        applications = VGroup(apps_title, app1, app2, app3).arrange(DOWN, aligned_edge=LEFT)
        applications.to_edge(DOWN)
        
        # Animate everything
        self.play(Write(title))
        self.play(Create(matrix_a))
        self.play(Write(exp_label))
        self.play(Write(times1), Create(matrix_b))
        self.play(Write(times2), Create(matrix_c), Write(times3))
        self.wait(2)
        
        self.play(Write(calc_title))
        self.play(Write(calc1))
        self.play(Write(calc2))
        self.play(Write(calc3))
        self.wait(2)
        
        self.play(Write(apps_title))
        self.play(Write(app1))
        self.play(Write(app2))
        self.play(Write(app3))
        self.wait(3)