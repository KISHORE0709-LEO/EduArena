from manim import *
import numpy as np

class BernoulliScene(Scene):
    def construct(self):
        title = Text("Bernoulli Distribution", font_size=48)
        self.play(Write(title))
        self.wait(1)
        
        # Parameters
        p = 0.3
        
        # Show probability
        prob_text = Text(f"p = {p}", font_size=36)
        prob_text.next_to(title, DOWN, buff=1)
        self.play(Write(prob_text))
        self.wait(1)
        
        # Show outcomes
        success = Text("Success (1)", color=GREEN, font_size=32)
        failure = Text("Failure (0)", color=RED, font_size=32)
        
        success.shift(LEFT * 3)
        failure.shift(RIGHT * 3)
        
        self.play(Write(success), Write(failure))
        self.wait(1)
        
        # Show probabilities
        p_success = Text(f"P(X=1) = {p}", color=GREEN, font_size=24)
        p_failure = Text(f"P(X=0) = {1-p}", color=RED, font_size=24)
        
        p_success.next_to(success, DOWN)
        p_failure.next_to(failure, DOWN)
        
        self.play(Write(p_success), Write(p_failure))
        self.wait(2)