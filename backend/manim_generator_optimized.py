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
                title = mn.Text(prompt[:40] + "..." if len(prompt) > 40 else prompt, font_size=24, color="#FFFFFF")
                title.to_edge(UP)
                self.play(mn.Write(title), run_time=1.5)
                self.wait(1)
                
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
                
                # Quick conclusion
                conclusion = mn.Text("Animation Complete!", font_size=18, color="#00FF00")
                conclusion.to_edge(DOWN)
                self.play(mn.Write(conclusion), run_time=1)
                self.wait(2)
            
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
                """Create optimized sorting animation"""
                intro = mn.Text("Bubble Sort", font_size=20, color="#00FFFF")
                intro.shift(UP * 1.5)
                self.play(mn.Write(intro), run_time=1)
                
                numbers = re.findall(r'\\d+', prompt)
                nums = [int(n) for n in numbers[:4]] if numbers else [4, 2, 7, 1]
                
                bars = mn.VGroup()
                for i, num in enumerate(nums):
                    bar = mn.Rectangle(width=0.8, height=num/3, color="#0066FF", fill_opacity=0.8)
                    bar.shift(LEFT * 1.5 + RIGHT * i * 1)
                    label = mn.Text(str(num), font_size=16, color="#FFFFFF")
                    label.next_to(bar, DOWN)
                    bars.add(mn.VGroup(bar, label))
                
                self.play(mn.Create(bars), run_time=2)
                
                # Quick sort demonstration
                for i in range(len(nums)):
                    for j in range(len(nums) - 1 - i):
                        if nums[j] > nums[j + 1]:
                            self.play(bars[j][0].animate.set_color("#FF0000"), bars[j+1][0].animate.set_color("#FF0000"), run_time=0.3)
                            self.play(
                                bars[j].animate.shift(RIGHT * 1),
                                bars[j+1].animate.shift(LEFT * 1),
                                run_time=0.8
                            )
                            bars[j], bars[j+1] = bars[j+1], bars[j]
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                            self.play(bars[j][0].animate.set_color("#00FF00"), bars[j+1][0].animate.set_color("#0066FF"), run_time=0.3)
                
                result = mn.Text("Sorted!", font_size=18, color="#00FF00")
                result.shift(DOWN * 2)
                self.play(mn.Write(result), run_time=1)
                self.wait(2)
            
            def _create_math_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create optimized math animation"""
                axes = mn.Axes(x_range=[-3, 3, 1], y_range=[-2, 2, 1], x_length=6, y_length=4)
                self.play(mn.Create(axes), run_time=2)
                
                if 'sine' in prompt.lower():
                    func = axes.plot(lambda x: np.sin(x), color="#FFFF00")
                    label = mn.MathTex(r"y = \\sin(x)", color="#FFFF00")
                elif 'cosine' in prompt.lower():
                    func = axes.plot(lambda x: np.cos(x), color="#00FF00")
                    label = mn.MathTex(r"y = \\cos(x)", color="#00FF00")
                else:
                    func = axes.plot(lambda x: x**2, color="#FF0000")
                    label = mn.MathTex(r"y = x^2", color="#FF0000")
                
                label.to_corner(UP + RIGHT)
                self.play(mn.Create(func), mn.Write(label), run_time=3)
                
                # Show key point
                point = mn.Dot(axes.coords_to_point(0, 0), color="#FFFFFF", radius=0.1)
                self.play(mn.Create(point), run_time=1)
                self.wait(2)
            
            def _create_physics_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create optimized physics animation"""
                if 'pendulum' in prompt.lower():
                    pivot = mn.Dot(UP * 2, color="#FFFFFF")
                    string = mn.Line(UP * 2, ORIGIN, color="#FFFFFF")
                    bob = mn.Circle(radius=0.2, color="#FFFF00", fill_opacity=1)
                    
                    pendulum = mn.VGroup(pivot, string, bob)
                    self.play(mn.Create(pendulum), run_time=2)
                    
                    # Simple swing
                    self.play(mn.Rotate(pendulum, angle=PI/6, about_point=UP * 2), run_time=1.5)
                    self.play(mn.Rotate(pendulum, angle=-PI/3, about_point=UP * 2), run_time=2)
                    self.play(mn.Rotate(pendulum, angle=PI/6, about_point=UP * 2), run_time=1.5)
                else:
                    box = mn.Square(side_length=1, color="#0066FF", fill_opacity=0.5)
                    arrow = mn.Arrow(box.get_right(), box.get_right() + RIGHT * 2, color="#FF0000")
                    force_label = mn.Text("F", color="#FF0000", font_size=20)
                    force_label.next_to(arrow, UP)
                    
                    self.play(mn.Create(box), run_time=1)
                    self.play(mn.Create(arrow), mn.Write(force_label), run_time=1.5)
                    self.play(box.animate.shift(RIGHT * 2), run_time=2)
                
                self.wait(2)
            
            def _create_data_structure_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create optimized data structure animation"""
                if 'tree' in prompt.lower():
                    root = mn.Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8)
                    root.shift(UP * 1)
                    root_label = mn.Text("1", font_size=16, color="#000000")
                    root_label.move_to(root.get_center())
                    
                    left = mn.Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8)
                    left.shift(LEFT * 1.5 + DOWN * 0.5)
                    left_label = mn.Text("2", font_size=16, color="#000000")
                    left_label.move_to(left.get_center())
                    
                    right = mn.Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8)
                    right.shift(RIGHT * 1.5 + DOWN * 0.5)
                    right_label = mn.Text("3", font_size=16, color="#000000")
                    right_label.move_to(right.get_center())
                    
                    edge1 = mn.Line(root.get_bottom(), left.get_top(), color="#FFFFFF")
                    edge2 = mn.Line(root.get_bottom(), right.get_top(), color="#FFFFFF")
                    
                    self.play(mn.Create(root), mn.Write(root_label), run_time=1)
                    self.play(mn.Create(edge1), mn.Create(left), mn.Write(left_label), run_time=1)
                    self.play(mn.Create(edge2), mn.Create(right), mn.Write(right_label), run_time=1)
                else:
                    # Simple linked list
                    nodes = []
                    for i in range(3):
                        node = mn.Rectangle(width=1, height=0.5, color="#0066FF", fill_opacity=0.7)
                        node.shift(LEFT * 1 + RIGHT * i * 1.5)
                        label = mn.Text(str(i+1), font_size=14, color="#FFFFFF")
                        label.move_to(node.get_center())
                        nodes.append(mn.VGroup(node, label))
                        
                        if i < 2:
                            arrow = mn.Arrow(node.get_right(), node.get_right() + RIGHT * 0.5, color="#FFFFFF")
                            self.play(mn.Create(nodes[i]), mn.Create(arrow), run_time=0.8)
                        else:
                            self.play(mn.Create(nodes[i]), run_time=0.8)
                
                self.wait(2)
            
            def _create_algorithm_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create optimized algorithm animation"""
                arr = [1, 3, 5, 7, 9]
                boxes = mn.VGroup()
                
                for i, val in enumerate(arr):
                    box = mn.Square(side_length=0.6, color="#0066FF", fill_opacity=0.3)
                    box.shift(LEFT * 2 + RIGHT * i * 0.8)
                    label = mn.Text(str(val), font_size=14, color="#FFFFFF")
                    label.move_to(box.get_center())
                    boxes.add(mn.VGroup(box, label))
                
                self.play(mn.Create(boxes), run_time=2)
                
                target = mn.Text("Search: 7", color="#FFFF00", font_size=16)
                target.to_edge(UP)
                self.play(mn.Write(target), run_time=1)
                
                # Quick binary search
                for i in [2, 3]:
                    self.play(boxes[i][0].animate.set_color("#FF0000"), run_time=0.5)
                    self.wait(0.8)
                    color = "#00FF00" if arr[i] == 7 else "#0066FF"
                    self.play(boxes[i][0].animate.set_color(color), run_time=0.5)
                
                found = mn.Text("Found!", color="#00FF00", font_size=16)
                found.shift(DOWN * 2)
                self.play(mn.Write(found), run_time=1)
                self.wait(2)
            
            def _create_general_animation(self, prompt, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                """Create optimized general animation"""
                words = prompt.lower().split()
                
                # Quick intro
                intro = mn.Text("Educational Animation", font_size=20, color="#00FFFF")
                intro.shift(UP * 2)
                self.play(mn.Write(intro), run_time=1.5)
                
                # Create shape based on prompt
                if any(word in words for word in ['circle', 'round', 'ball']):
                    shape = mn.Circle(radius=1.2, color="#0066FF", fill_opacity=0.6)
                    shape_name = "Circle"
                    properties = ["Radius = r", "Area = πr²", "Circumference = 2πr"]
                elif any(word in words for word in ['square', 'box', 'rectangle']):
                    shape = mn.Square(side_length=2, color="#00FF00", fill_opacity=0.6)
                    shape_name = "Square"
                    properties = ["Side = s", "Area = s²", "Perimeter = 4s"]
                elif any(word in words for word in ['triangle']):
                    shape = mn.Triangle(color="#FF0000", fill_opacity=0.6)
                    shape_name = "Triangle"
                    properties = ["3 sides", "3 angles", "Sum = 180°"]
                elif any(word in words for word in ['dna', 'biology']):
                    # Simple DNA representation
                    helix1 = mn.ParametricFunction(lambda t: np.array([t/3, np.sin(t)/2, 0]), t_range=[-2*PI, 2*PI], color="#FF0000")
                    helix2 = mn.ParametricFunction(lambda t: np.array([t/3, -np.sin(t)/2, 0]), t_range=[-2*PI, 2*PI], color="#0000FF")
                    shape = mn.VGroup(helix1, helix2)
                    shape_name = "DNA"
                    properties = ["Double helix", "Genetic code", "Life blueprint"]
                elif any(word in words for word in ['atom', 'molecule']):
                    # Simple atom
                    nucleus = mn.Circle(radius=0.3, color="#FFFF00", fill_opacity=1)
                    electron1 = mn.Circle(radius=0.1, color="#0066FF", fill_opacity=1)
                    electron1.shift(RIGHT * 1.5)
                    electron2 = mn.Circle(radius=0.1, color="#0066FF", fill_opacity=1)
                    electron2.shift(LEFT * 1.5)
                    orbit = mn.Circle(radius=1.5, color="#FFFFFF", fill_opacity=0)
                    shape = mn.VGroup(nucleus, electron1, electron2, orbit)
                    shape_name = "Atom"
                    properties = ["Nucleus + electrons", "Chemical bonds", "Matter building block"]
                else:
                    shape = mn.RegularPolygon(n=6, color="#FFFF00", fill_opacity=0.7)
                    shape_name = "Hexagon"
                    properties = ["6 sides", "Regular polygon", "Symmetric"]
                
                # Show shape name
                name_text = mn.Text(shape_name, font_size=18, color="#FFFFFF")
                name_text.shift(UP * 0.5)
                self.play(mn.Write(name_text), run_time=1)
                
                # Create shape
                self.play(mn.Create(shape), run_time=2)
                self.wait(1)
                
                # Show properties quickly
                for i, prop in enumerate(properties[:2]):  # Only show 2 properties
                    prop_text = mn.Text(prop, font_size=14, color="#FFFF00")
                    prop_text.shift(DOWN * (1.5 + i * 0.4))
                    self.play(mn.Write(prop_text), run_time=1)
                
                # Quick animations
                self.play(shape.animate.scale(1.3), run_time=1)
                self.play(mn.Rotate(shape, angle=PI), run_time=1.5)
                self.play(shape.animate.scale(0.8), run_time=1)
                
                # Color change
                if hasattr(shape, 'set_color'):
                    self.play(shape.animate.set_color("#FF00FF"), run_time=1)
                
                self.wait(2)
        
        return DynamicScene
    
    def _render_scene(self, scene_class, animation_id: str) -> str:
        """Render the Manim scene and return video path"""
        
        # Configure Manim for faster rendering
        mn.config.media_dir = self.output_dir
        mn.config.video_dir = os.path.join(self.output_dir, "videos")
        mn.config.quality = "low_quality"  # Faster rendering
        mn.config.format = "mp4"
        mn.config.frame_rate = 15  # Lower frame rate for speed
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