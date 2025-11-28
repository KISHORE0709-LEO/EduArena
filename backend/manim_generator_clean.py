import manim as mn
import tempfile
import os
from typing import Dict, Any
import json
import re
import numpy as np

class TextToAnimationGenerator:
    def __init__(self):
        self.output_dir = "media"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_animation(self, prompt: str, animation_id: str) -> str:
        """Generate Manim animation for ANY text prompt"""
        
        # Create dynamic scene class for this specific prompt
        scene_class = self._create_dynamic_scene(prompt)
        
        # Generate animation
        video_path = self._render_scene(scene_class, animation_id)
        
        return video_path
    
    def _create_dynamic_scene(self, prompt: str):
        """Create a dynamic Manim scene for any prompt"""
        
        class DynamicScene(mn.Scene):
            def construct(self):
                # Define constants
                UP = np.array([0, 1, 0])
                DOWN = np.array([0, -1, 0])
                LEFT = np.array([-1, 0, 0])
                RIGHT = np.array([1, 0, 0])
                ORIGIN = np.array([0, 0, 0])
                PI = np.pi
                
                # Create title
                title = mn.Text(prompt[:50] + "..." if len(prompt) > 50 else prompt, font_size=20, color="#FFFFFF")
                title.to_edge(UP)
                self.play(mn.Write(title), run_time=1)
                self.wait(0.5)
                
                # Generate content based on prompt analysis
                if self._is_sorting_prompt(prompt):
                    self._create_sorting_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                elif self._is_math_prompt(prompt):
                    self._create_math_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                elif self._is_physics_prompt(prompt):
                    self._create_physics_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                elif self._is_data_structure_prompt(prompt):
                    self._create_data_structure_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                elif self._is_algorithm_prompt(prompt):
                    self._create_algorithm_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                else:
                    self._create_general_animation(prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
                
                # Add conclusion
                conclusion = mn.Text("Animation Complete!", font_size=18, color="#00FF00")
                conclusion.to_edge(DOWN)
                self.play(mn.Write(conclusion), run_time=1)
                self.wait(3)  # Extended final wait
            
            def _is_sorting_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['sort', 'bubble', 'merge', 'quick'])
            
            def _is_math_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['function', 'graph', 'plot', 'sine', 'cosine', 'equation'])
            
            def _is_physics_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['force', 'pendulum', 'gravity', 'motion'])
            
            def _is_data_structure_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['tree', 'linked', 'stack', 'queue', 'array'])
            
            def _is_algorithm_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['search', 'binary', 'algorithm'])
            
            def _create_sorting_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create comprehensive sorting animation with educational content"""
                # Introduction
                intro = mn.Text("Bubble Sort Algorithm", font_size=24, color="#00FFFF")
                intro.shift(UP * 3)
                self.play(mn.Write(intro), run_time=2)
                self.wait(1)
                
                explanation = mn.Text("Compares adjacent elements and swaps if needed", font_size=16, color="#FFFF00")
                explanation.shift(UP * 2.5)
                self.play(mn.Write(explanation), run_time=2)
                self.wait(2)
                
                numbers = re.findall(r'\\d+', prompt)
                if numbers:
                    nums = [int(n) for n in numbers[:6]]
                else:
                    nums = [64, 34, 25, 12, 22, 11]
                
                # Show original array
                original_text = mn.Text(f"Original Array: {nums}", font_size=18, color="#FFFFFF")
                original_text.shift(UP * 2)
                self.play(mn.Write(original_text), run_time=2)
                self.wait(2)
                
                bars = mn.VGroup()
                labels = mn.VGroup()
                
                for i, num in enumerate(nums):
                    bar = mn.Rectangle(width=0.7, height=num/15, color="#0066FF", fill_opacity=0.8)
                    bar.shift(LEFT * 2.5 + RIGHT * i * 0.9)
                    label = mn.Text(str(num), font_size=18, color="#FFFFFF")
                    label.next_to(bar, DOWN)
                    bars.add(bar)
                    labels.add(label)
                
                self.play(mn.Create(bars), mn.Write(labels), run_time=3)
                self.wait(2)
                
                # Step counter
                step_counter = mn.Text("Step: 0", font_size=16, color="#00FF00")
                step_counter.to_edge(LEFT + UP)
                self.play(mn.Write(step_counter), run_time=1)
                
                comparison_counter = mn.Text("Comparisons: 0", font_size=16, color="#FF00FF")
                comparison_counter.next_to(step_counter, DOWN)
                self.play(mn.Write(comparison_counter), run_time=1)
                
                step_count = 0
                comparison_count = 0
                
                # Detailed bubble sort with explanations
                for i in range(len(nums)):
                    pass_text = mn.Text(f"Pass {i+1}: Finding largest element", font_size=14, color="#FFAA00")
                    pass_text.shift(DOWN * 3)
                    self.play(mn.Write(pass_text), run_time=1)
                    
                    for j in range(len(nums) - 1 - i):
                        step_count += 1
                        comparison_count += 1
                        
                        # Update counters
                        new_step = mn.Text(f"Step: {step_count}", font_size=16, color="#00FF00")
                        new_step.to_edge(LEFT + UP)
                        new_comparison = mn.Text(f"Comparisons: {comparison_count}", font_size=16, color="#FF00FF")
                        new_comparison.next_to(new_step, DOWN)
                        
                        self.play(
                            mn.Transform(step_counter, new_step),
                            mn.Transform(comparison_counter, new_comparison),
                            run_time=0.5
                        )
                        
                        # Highlight comparison
                        compare_text = mn.Text(f"Comparing {nums[j]} and {nums[j+1]}", font_size=12, color="#FFFFFF")
                        compare_text.shift(DOWN * 3.5)
                        self.play(mn.Write(compare_text), run_time=0.8)
                        
                        self.play(
                            bars[j].animate.set_color("#FFFF00"), 
                            bars[j+1].animate.set_color("#FFFF00"), 
                            run_time=0.8
                        )
                        self.wait(1)
                        
                        if nums[j] > nums[j + 1]:
                            # Show swap decision
                            swap_text = mn.Text(f"{nums[j]} > {nums[j+1]}, SWAP!", font_size=12, color="#FF0000")
                            swap_text.shift(DOWN * 4)
                            self.play(mn.Write(swap_text), run_time=1)
                            
                            self.play(bars[j].animate.set_color("#FF0000"), bars[j+1].animate.set_color("#FF0000"), run_time=0.5)
                            
                            # Animate swap
                            self.play(
                                bars[j].animate.shift(RIGHT * 0.9),
                                bars[j+1].animate.shift(LEFT * 0.9),
                                labels[j].animate.shift(RIGHT * 0.9),
                                labels[j+1].animate.shift(LEFT * 0.9),
                                run_time=1.5
                            )
                            
                            # Update arrays
                            bars[j], bars[j+1] = bars[j+1], bars[j]
                            labels[j], labels[j+1] = labels[j+1], labels[j]
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                            
                            self.play(bars[j].animate.set_color("#00FF00"), bars[j+1].animate.set_color("#00FF00"), run_time=0.5)
                            self.play(mn.FadeOut(swap_text), run_time=0.5)
                        else:
                            # Show no swap decision
                            no_swap_text = mn.Text(f"{nums[j]} <= {nums[j+1]}, No swap", font_size=12, color="#00FF00")
                            no_swap_text.shift(DOWN * 4)
                            self.play(mn.Write(no_swap_text), run_time=1)
                            self.play(bars[j].animate.set_color("#0066FF"), bars[j+1].animate.set_color("#0066FF"), run_time=0.5)
                            self.play(mn.FadeOut(no_swap_text), run_time=0.5)
                        
                        self.play(mn.FadeOut(compare_text), run_time=0.3)
                        self.wait(0.5)
                    
                    # Mark sorted element
                    sorted_text = mn.Text(f"Element {nums[len(nums)-1-i]} is now in correct position", font_size=12, color="#00FF00")
                    sorted_text.shift(DOWN * 3.2)
                    self.play(mn.Write(sorted_text), run_time=1.5)
                    self.play(bars[len(nums)-1-i].animate.set_color("#00AA00"), run_time=1)
                    self.play(mn.FadeOut(pass_text), mn.FadeOut(sorted_text), run_time=1)
                    self.wait(1)
                
                # Final result
                final_text = mn.Text("Sorting Complete!", font_size=20, color="#00FF00")
                final_text.shift(DOWN * 3)
                self.play(mn.Write(final_text), run_time=2)
                
                sorted_array_text = mn.Text(f"Sorted Array: {nums}", font_size=16, color="#FFFF00")
                sorted_array_text.shift(DOWN * 3.5)
                self.play(mn.Write(sorted_array_text), run_time=2)
                
                # Complexity analysis
                complexity_title = mn.Text("Algorithm Analysis:", font_size=16, color="#FF00FF")
                complexity_title.to_edge(RIGHT + UP)
                self.play(mn.Write(complexity_title), run_time=1.5)
                
                complexity_info = [
                    "Time Complexity: O(n²)",
                    f"Total Comparisons: {comparison_count}",
                    "Space Complexity: O(1)",
                    "Stable: Yes"
                ]
                
                for i, info in enumerate(complexity_info):
                    info_text = mn.Text(info, font_size=12, color="#FFFFFF")
                    info_text.next_to(complexity_title, DOWN * (i + 1))
                    self.play(mn.Write(info_text), run_time=1)
                    self.wait(0.5)
                
                self.wait(4)
            
            def _create_math_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create comprehensive mathematical animation"""
                # Introduction
                intro = mn.Text("Mathematical Function Visualization", font_size=22, color="#00FFFF")
                intro.shift(UP * 3.5)
                self.play(mn.Write(intro), run_time=2)
                self.wait(1.5)
                
                # Create coordinate system with labels
                axes = mn.Axes(
                    x_range=[-4, 4, 1], 
                    y_range=[-3, 3, 1], 
                    x_length=8, 
                    y_length=6, 
                    axis_config={"color": "#FFFFFF", "include_numbers": True}
                )
                
                axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
                
                self.play(mn.Create(axes), mn.Write(axes_labels), run_time=3)
                self.wait(2)
                
                # Determine function type and create comprehensive visualization
                if 'sine' in prompt.lower() or 'sin' in prompt.lower():
                    func_name = "Sine Function"
                    func_equation = r"y = \sin(x)"
                    func_color = "#FFFF00"
                    
                    # Create function step by step
                    explanation = mn.Text("The sine function: periodic, oscillating between -1 and 1", 
                                        font_size=14, color="#FFFFFF")
                    explanation.shift(UP * 2.8)
                    self.play(mn.Write(explanation), run_time=2.5)
                    self.wait(2)
                    
                    # Plot function gradually
                    func = axes.plot(lambda x: np.sin(x), color=func_color, x_range=[-4, 4])
                    self.play(mn.Create(func), run_time=4)
                    
                    # Show key points
                    key_points = [
                        (0, 0, "Origin (0,0)"),
                        (PI/2, 1, "Maximum (π/2, 1)"),
                        (PI, 0, "Zero (π, 0)"),
                        (3*PI/2, -1, "Minimum (3π/2, -1)")
                    ]
                    
                    for x, y, label_text in key_points:
                        if -4 <= x <= 4:
                            point = mn.Dot(axes.coords_to_point(x, y), color="#FF0000", radius=0.08)
                            point_label = mn.Text(label_text, font_size=10, color="#FF0000")
                            point_label.next_to(point, UP if y >= 0 else DOWN)
                            self.play(mn.Create(point), mn.Write(point_label), run_time=1.5)
                            self.wait(1)
                    
                    # Properties
                    properties = [
                        "Period: 2π",
                        "Amplitude: 1",
                        "Domain: All real numbers",
                        "Range: [-1, 1]"
                    ]
                    
                elif 'cosine' in prompt.lower() or 'cos' in prompt.lower():
                    func_name = "Cosine Function"
                    func_equation = r"y = \cos(x)"
                    func_color = "#00FF00"
                    
                    explanation = mn.Text("The cosine function: periodic, starts at maximum", 
                                        font_size=14, color="#FFFFFF")
                    explanation.shift(UP * 2.8)
                    self.play(mn.Write(explanation), run_time=2.5)
                    self.wait(2)
                    
                    func = axes.plot(lambda x: np.cos(x), color=func_color, x_range=[-4, 4])
                    self.play(mn.Create(func), run_time=4)
                    
                    properties = [
                        "Period: 2π",
                        "Amplitude: 1",
                        "Phase shift: π/2 from sine",
                        "Even function: cos(-x) = cos(x)"
                    ]
                    
                elif 'quadratic' in prompt.lower() or 'parabola' in prompt.lower() or 'x^2' in prompt.lower():
                    func_name = "Quadratic Function"
                    func_equation = r"y = x^2"
                    func_color = "#FF0000"
                    
                    explanation = mn.Text("The quadratic function: U-shaped curve (parabola)", 
                                        font_size=14, color="#FFFFFF")
                    explanation.shift(UP * 2.8)
                    self.play(mn.Write(explanation), run_time=2.5)
                    self.wait(2)
                    
                    func = axes.plot(lambda x: x**2, color=func_color, x_range=[-3, 3])
                    self.play(mn.Create(func), run_time=4)
                    
                    # Show vertex
                    vertex = mn.Dot(axes.coords_to_point(0, 0), color="#FFFF00", radius=0.1)
                    vertex_label = mn.Text("Vertex (0,0)", font_size=12, color="#FFFF00")
                    vertex_label.next_to(vertex, DOWN)
                    self.play(mn.Create(vertex), mn.Write(vertex_label), run_time=1.5)
                    
                    properties = [
                        "Vertex: (0, 0)",
                        "Opens upward",
                        "Axis of symmetry: y-axis",
                        "Domain: All real numbers",
                        "Range: [0, ∞)"
                    ]
                    
                else:
                    # Default: cubic function
                    func_name = "Cubic Function"
                    func_equation = r"y = x^3"
                    func_color = "#FF00FF"
                    
                    explanation = mn.Text("The cubic function: S-shaped curve", 
                                        font_size=14, color="#FFFFFF")
                    explanation.shift(UP * 2.8)
                    self.play(mn.Write(explanation), run_time=2.5)
                    self.wait(2)
                    
                    func = axes.plot(lambda x: x**3, color=func_color, x_range=[-2, 2])
                    self.play(mn.Create(func), run_time=4)
                    
                    properties = [
                        "Odd function: f(-x) = -f(x)",
                        "Inflection point: (0,0)",
                        "Domain: All real numbers",
                        "Range: All real numbers"
                    ]
                
                # Show equation
                equation = mn.MathTex(func_equation, color=func_color, font_size=48)
                equation.to_corner(UP + RIGHT)
                self.play(mn.Write(equation), run_time=2)
                self.wait(2)
                
                # Function name
                name_text = mn.Text(func_name, font_size=18, color=func_color)
                name_text.next_to(equation, DOWN)
                self.play(mn.Write(name_text), run_time=1.5)
                self.wait(1)
                
                # Show properties
                prop_title = mn.Text("Properties:", font_size=16, color="#FFFFFF")
                prop_title.to_edge(LEFT + DOWN)
                self.play(mn.Write(prop_title), run_time=1)
                
                for i, prop in enumerate(properties):
                    prop_text = mn.Text(f"• {prop}", font_size=12, color="#FFFF00")
                    prop_text.next_to(prop_title, DOWN * (i + 1))
                    self.play(mn.Write(prop_text), run_time=1.2)
                    self.wait(0.8)
                
                # Interactive demonstration
                demo_title = mn.Text("Interactive Demonstration:", font_size=16, color="#00FFFF")
                demo_title.shift(DOWN * 2.5)
                self.play(mn.Write(demo_title), run_time=1.5)
                
                # Animate a point moving along the curve
                if 'sine' in prompt.lower() or 'cosine' in prompt.lower():
                    moving_point = mn.Dot(color="#FF0000", radius=0.08)
                    trace = mn.TracedPath(moving_point.get_center, stroke_color="#FF0000", stroke_width=3)
                    self.add(trace)
                    
                    def update_point(mob, dt):
                        t = self.renderer.time * 2
                        if 'sine' in prompt.lower():
                            y = np.sin(t)
                        else:
                            y = np.cos(t)
                        new_pos = axes.coords_to_point(t % (2*PI) - PI, y)
                        mob.move_to(new_pos)
                    
                    moving_point.add_updater(update_point)
                    self.add(moving_point)
                    self.wait(8)
                    moving_point.remove_updater(update_point)
                
                self.wait(3)
            
            def _create_physics_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create physics animation"""
                if 'pendulum' in prompt.lower():
                    pivot = mn.Dot(UP * 2, color="#FFFFFF")
                    string = mn.Line(UP * 2, DOWN * 0.5, color="#FFFFFF")
                    bob = mn.Circle(radius=0.2, color="#FFFF00", fill_opacity=1)
                    bob.move_to(DOWN * 0.5)
                    
                    pendulum = mn.VGroup(pivot, string, bob)
                    self.play(mn.Create(pendulum))
                    
                    self.play(mn.Rotate(pendulum, angle=PI/4, about_point=UP * 2), run_time=1)
                    self.play(mn.Rotate(pendulum, angle=-PI/2, about_point=UP * 2), run_time=2)
                    self.play(mn.Rotate(pendulum, angle=PI/4, about_point=UP * 2), run_time=1)
                else:
                    box = mn.Square(side_length=1, color="#0066FF", fill_opacity=0.5)
                    force_arrow = mn.Arrow(box.get_right(), box.get_right() + RIGHT * 2, color="#FF0000")
                    force_label = mn.Text("F", color="#FF0000", font_size=24)
                    force_label.next_to(force_arrow, UP)
                    
                    self.play(mn.Create(box))
                    self.play(mn.Create(force_arrow), mn.Write(force_label))
                    self.play(box.animate.shift(RIGHT * 2), run_time=2)
            
            def _create_data_structure_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create data structure animation"""
                if 'tree' in prompt.lower():
                    nodes = [mn.Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8) for _ in range(3)]
                    labels = [mn.Text(str(i+1), font_size=16, color="#000000") for i in range(3)]
                    
                    nodes[0].shift(UP * 1.5)
                    nodes[1].shift(LEFT * 1.5 + UP * 0.5)
                    nodes[2].shift(RIGHT * 1.5 + UP * 0.5)
                    
                    for i, (node, label) in enumerate(zip(nodes, labels)):
                        label.move_to(node.get_center())
                        self.play(mn.Create(node), mn.Write(label), run_time=0.5)
                        
                    edges = [
                        mn.Line(nodes[0].get_bottom(), nodes[1].get_top(), color="#FFFFFF"),
                        mn.Line(nodes[0].get_bottom(), nodes[2].get_top(), color="#FFFFFF")
                    ]
                    self.play(*[mn.Create(edge) for edge in edges])
                else:
                    nodes = [mn.Rectangle(width=1, height=0.5, color="#0066FF", fill_opacity=0.7) for _ in range(3)]
                    arrows = [mn.Arrow(ORIGIN, RIGHT * 0.5, color="#FFFFFF") for _ in range(2)]
                    
                    for i, node in enumerate(nodes):
                        node.shift(LEFT * 1 + RIGHT * i * 1.5)
                        if i < 2:
                            arrows[i].next_to(node, RIGHT, buff=0.1)
                    
                    for node, arrow in zip(nodes[:-1], arrows):
                        self.play(mn.Create(node), mn.Create(arrow), run_time=0.5)
                    self.play(mn.Create(nodes[-1]))
            
            def _create_algorithm_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create algorithm animation"""
                arr = [1, 3, 5, 7, 9]
                boxes = mn.VGroup()
                
                for i, val in enumerate(arr):
                    box = mn.Square(side_length=0.6, color="#0066FF", fill_opacity=0.3)
                    box.shift(LEFT * 2 + RIGHT * i * 0.8)
                    label = mn.Text(str(val), font_size=14, color="#FFFFFF")
                    label.move_to(box.get_center())
                    boxes.add(mn.VGroup(box, label))
                
                self.play(mn.Create(boxes))
                
                target = mn.Text("Target: 7", color="#FFFF00", font_size=20)
                target.to_edge(UP)
                self.play(mn.Write(target))
                
                for i in [2, 3]:
                    self.play(boxes[i][0].animate.set_color("#FF0000"), run_time=0.5)
                    self.wait(0.5)
                    final_color = "#00FF00" if arr[i] == 7 else "#0066FF"
                    self.play(boxes[i][0].animate.set_color(final_color), run_time=0.5)
            
            def _create_general_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create comprehensive general animation for any prompt"""
                words = prompt.lower().split()
                
                # Extended introduction
                explanation = mn.Text("Educational Animation:", font_size=24, color="#00FFFF")
                explanation.shift(UP * 2.5)
                self.play(mn.Write(explanation), run_time=1.5)
                self.wait(1)
                
                # Show the prompt
                prompt_text = mn.Text(f'"{prompt}"', font_size=18, color="#FFFF00")
                prompt_text.shift(UP * 1.8)
                self.play(mn.Write(prompt_text), run_time=2)
                self.wait(1.5)
                
                # Create and analyze shape
                if any(word in words for word in ['circle', 'round', 'ball', 'sphere']):
                    shape = mn.Circle(radius=1.2, color="#0066FF", fill_opacity=0.6)
                    shape_name = "Circle"
                    properties = ["Radius = r", "Area = πr²", "Circumference = 2πr"]
                elif any(word in words for word in ['square', 'box', 'rectangle', 'cube']):
                    shape = mn.Square(side_length=2, color="#00FF00", fill_opacity=0.6)
                    shape_name = "Square"
                    properties = ["Side length = s", "Area = s²", "Perimeter = 4s"]
                elif any(word in words for word in ['triangle', 'pyramid']):
                    shape = mn.Triangle(color="#FF0000", fill_opacity=0.6)
                    shape_name = "Triangle"
                    properties = ["3 sides", "3 angles", "Sum of angles = 180°"]
                elif any(word in words for word in ['star', 'asterisk']):
                    shape = mn.Star(color="#FFFF00", fill_opacity=0.7, outer_radius=1.5)
                    shape_name = "Star"
                    properties = ["Multiple points", "Symmetrical", "Decorative shape"]
                elif any(word in words for word in ['dna', 'helix', 'biology']):
                    # Create DNA double helix
                    helix1 = mn.ParametricFunction(
                        lambda t: np.array([t/2, np.sin(t), 0]), 
                        t_range=[-4*PI, 4*PI], 
                        color="#FF0000"
                    )
                    helix2 = mn.ParametricFunction(
                        lambda t: np.array([t/2, -np.sin(t), 0]), 
                        t_range=[-4*PI, 4*PI], 
                        color="#0000FF"
                    )
                    shape = mn.VGroup(helix1, helix2)
                    shape_name = "DNA Double Helix"
                    properties = ["Genetic material", "Double strand", "Contains genes"]
                elif any(word in words for word in ['atom', 'molecule', 'chemistry']):
                    # Create atomic structure
                    nucleus = mn.Circle(radius=0.3, color="#FFFF00", fill_opacity=1)
                    electrons = []
                    for i in range(3):
                        electron = mn.Circle(radius=0.1, color="#0066FF", fill_opacity=1)
                        angle = i * 2 * PI / 3
                        electron.shift(1.8 * np.cos(angle) * RIGHT + 1.8 * np.sin(angle) * UP)
                        electrons.append(electron)
                    
                    # Electron orbits
                    orbit1 = mn.Circle(radius=1.2, color="#FFFFFF", fill_opacity=0)
                    orbit2 = mn.Circle(radius=1.8, color="#FFFFFF", fill_opacity=0)
                    
                    shape = mn.VGroup(nucleus, orbit1, orbit2, *electrons)
                    shape_name = "Atomic Structure"
                    properties = ["Nucleus + Electrons", "Electron orbits", "Chemical bonds"]
                elif any(word in words for word in ['cell', 'biology', 'life']):
                    # Create cell structure
                    cell_wall = mn.Circle(radius=2, color="#00FF00", fill_opacity=0.2)
                    nucleus = mn.Circle(radius=0.6, color="#FF0000", fill_opacity=0.7)
                    mitochondria = [mn.Ellipse(width=0.4, height=0.2, color="#FF00FF", fill_opacity=0.8) for _ in range(3)]
                    
                    for i, mito in enumerate(mitochondria):
                        angle = i * 2 * PI / 3 + PI/6
                        mito.shift(1.2 * np.cos(angle) * RIGHT + 1.2 * np.sin(angle) * UP)
                    
                    shape = mn.VGroup(cell_wall, nucleus, *mitochondria)
                    shape_name = "Biological Cell"
                    properties = ["Cell membrane", "Nucleus (DNA)", "Mitochondria (energy)"]
                else:
                    # Default comprehensive shape
                    shape = mn.RegularPolygon(n=8, color="#FFFF00", fill_opacity=0.7, radius=1.5)
                    shape_name = "Octagon"
                    properties = ["8 sides", "Regular polygon", "Symmetrical"]
                
                # Introduce the shape
                intro_text = mn.Text(f"Let's explore: {shape_name}", font_size=20, color="#FFFFFF")
                intro_text.shift(UP * 0.5)
                self.play(mn.Write(intro_text), run_time=2)
                self.wait(1)
                
                # Create the shape with dramatic effect
                self.play(mn.Create(shape), run_time=3)
                self.wait(2)
                
                # Show properties one by one
                property_texts = []
                for i, prop in enumerate(properties):
                    prop_text = mn.Text(prop, font_size=16, color="#00FFFF")
                    prop_text.shift(DOWN * (1.5 + i * 0.4))
                    property_texts.append(prop_text)
                    self.play(mn.Write(prop_text), run_time=1.5)
                    self.wait(1)
                
                # Comprehensive animation sequence
                self.wait(1)
                
                # Animation 1: Scale transformation
                scale_text = mn.Text("Scaling transformation", font_size=14, color="#FFAA00")
                scale_text.to_edge(LEFT + UP)
                self.play(mn.Write(scale_text), run_time=1)
                self.play(shape.animate.scale(1.8), run_time=2)
                self.wait(1)
                self.play(shape.animate.scale(1/1.8), run_time=2)
                self.wait(1)
                
                # Animation 2: Rotation
                rotate_text = mn.Text("Rotation transformation", font_size=14, color="#FFAA00")
                rotate_text.next_to(scale_text, DOWN)
                self.play(mn.Write(rotate_text), run_time=1)
                self.play(mn.Rotate(shape, angle=2*PI), run_time=4)
                self.wait(1)
                
                # Animation 3: Color changes
                color_text = mn.Text("Color variations", font_size=14, color="#FFAA00")
                color_text.next_to(rotate_text, DOWN)
                self.play(mn.Write(color_text), run_time=1)
                
                colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
                for color in colors:
                    self.play(shape.animate.set_color(color), run_time=0.8)
                    self.wait(0.5)
                
                # Animation 4: Movement patterns
                move_text = mn.Text("Movement patterns", font_size=14, color="#FFAA00")
                move_text.next_to(color_text, DOWN)
                self.play(mn.Write(move_text), run_time=1)
                
                # Circular motion
                self.play(shape.animate.shift(RIGHT * 2), run_time=1.5)
                self.play(shape.animate.shift(UP * 2), run_time=1.5)
                self.play(shape.animate.shift(LEFT * 4), run_time=1.5)
                self.play(shape.animate.shift(DOWN * 4), run_time=1.5)
                self.play(shape.animate.shift(RIGHT * 4), run_time=1.5)
                self.play(shape.animate.shift(UP * 2), run_time=1.5)
                self.play(shape.animate.shift(LEFT * 2), run_time=1.5)
                
                # Final educational summary
                self.wait(2)
                summary_title = mn.Text("Educational Summary:", font_size=18, color="#00FF00")
                summary_title.shift(UP * 3)
                self.play(mn.Write(summary_title), run_time=1.5)
                
                summary_points = [
                    f"• Explored {shape_name} properties",
                    "• Demonstrated transformations",
                    "• Showed color theory",
                    "• Illustrated movement physics"
                ]
                
                summary_texts = []
                for i, point in enumerate(summary_points):
                    point_text = mn.Text(point, font_size=14, color="#FFFFFF")
                    point_text.shift(UP * (2 - i * 0.5))
                    summary_texts.append(point_text)
                    self.play(mn.Write(point_text), run_time=1.2)
                    self.wait(0.8)
                
                # Final message
                self.wait(2)
                final_msg = mn.Text("Thank you for learning!", font_size=20, color="#FFFF00")
                final_msg.shift(DOWN * 2.5)
                self.play(mn.Write(final_msg), run_time=2)
                self.wait(3)
        
        return DynamicScene
    
    def _render_scene(self, scene_class, animation_id: str) -> str:
        """Render the Manim scene and return video path"""
        
        # Configure Manim for web output
        mn.config.media_dir = self.output_dir
        mn.config.video_dir = os.path.join(self.output_dir, "videos")
        mn.config.quality = "medium_quality"
        mn.config.format = "mp4"
        mn.config.frame_rate = 30
        mn.config.background_color = "#000000"
        
        # Create and render scene
        scene = scene_class()
        scene.render()
        
        # Find the generated video file
        video_files = []
        for root, dirs, files in os.walk(mn.config.video_dir):
            for file in files:
                if file.endswith('.mp4'):
                    video_files.append(os.path.join(root, file))
        
        if video_files:
            # Get the most recent video file
            latest_video = max(video_files, key=os.path.getctime)
            
            # Copy to a predictable location
            final_path = os.path.join(self.output_dir, f"{animation_id}.mp4")
            import shutil
            shutil.copy2(latest_video, final_path)
            
            return final_path
        
        return None