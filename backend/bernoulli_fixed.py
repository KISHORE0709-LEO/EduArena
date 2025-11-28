from manim import *
import numpy as np

class BernoulliScene(Scene):
    def construct(self):
        title = Text("Bernoulli's Principle", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        
        # Draw pipe sections
        wide_pipe = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        narrow_pipe = Rectangle(width=2, height=0.8, color=BLUE, fill_opacity=0.3)
        
        wide_pipe.shift(LEFT * 2)
        narrow_pipe.shift(RIGHT * 1)
        
        self.play(Create(wide_pipe), Create(narrow_pipe))
        self.wait(1)
        
        # Velocity arrows
        v1_arrow = Arrow(LEFT, RIGHT, color=GREEN).scale(0.8)
        v1_arrow.next_to(wide_pipe, UP)
        v1_label = Text("v1 (slow)", font_size=20, color=GREEN)
        v1_label.next_to(v1_arrow, UP)
        
        v2_arrow = Arrow(LEFT, RIGHT, color=RED).scale(1.5)
        v2_arrow.next_to(narrow_pipe, UP)
        v2_label = Text("v2 (fast)", font_size=20, color=RED)
        v2_label.next_to(v2_arrow, UP)
        
        self.play(Create(v1_arrow), Write(v1_label))
        self.play(Create(v2_arrow), Write(v2_label))
        self.wait(1)
        
        # Pressure indicators
        p1_text = Text("High Pressure", font_size=18, color=YELLOW)
        p1_text.next_to(wide_pipe, DOWN)
        
        p2_text = Text("Low Pressure", font_size=18, color=ORANGE)
        p2_text.next_to(narrow_pipe, DOWN)
        
        self.play(Write(p1_text), Write(p2_text))
        self.wait(2)