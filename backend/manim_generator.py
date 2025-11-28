from manim import *
from manim import config
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
        
        class DynamicScene(Scene):
            def construct(self):
                # Create title
                title = Text(prompt[:50] + "..." if len(prompt) > 50 else prompt, font_size=20, color="#FFFFFF")
                title.to_edge(UP)
                self.play(Write(title), run_time=1)
                self.wait(0.5)
                
                # Generate content based on prompt analysis
                if self._is_sorting_prompt(prompt):
                    self._create_sorting_animation(prompt)
                elif self._is_math_prompt(prompt):
                    self._create_math_animation(prompt)
                elif self._is_physics_prompt(prompt):
                    self._create_physics_animation(prompt)
                elif self._is_data_structure_prompt(prompt):
                    self._create_data_structure_animation(prompt)
                elif self._is_algorithm_prompt(prompt):
                    self._create_algorithm_animation(prompt)
                else:
                    self._create_general_animation(prompt)
                
                self.wait(2)
            
            def _is_sorting_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['sort', 'bubble', 'merge', 'quick'])
            
            def _is_math_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['function', 'graph', 'plot', 'sine', 'cosine', 'equation', 'derivative'])
            
            def _is_physics_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['force', 'pendulum', 'gravity', 'motion', 'velocity', 'acceleration'])
            
            def _is_data_structure_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['tree', 'linked', 'stack', 'queue', 'array', 'node'])
            
            def _is_algorithm_prompt(self, prompt):
                return any(word in prompt.lower() for word in ['search', 'binary', 'algorithm', 'bfs', 'dfs'])
            
            def _create_sorting_animation(self, prompt):
                """Create sorting animation"""
                numbers = re.findall(r'\d+', prompt)
                if numbers:
                    nums = [int(n) for n in numbers[:5]]
                else:
                    nums = [64, 34, 25, 12, 22]
                
                bars = VGroup()
                labels = VGroup()
                
                for i, num in enumerate(nums):
                    bar = Rectangle(width=0.6, height=num/20, color="#0066FF", fill_opacity=0.7)
                    bar.shift(LEFT * 2 + RIGHT * i * 0.8)
                    label = Text(str(num), font_size=16, color="#FFFFFF").next_to(bar, DOWN)
                    bars.add(bar)
                    labels.add(label)
                
                self.play(Create(bars), Write(labels))
                
                # Simple bubble sort
                for i in range(len(nums)):
                    for j in range(len(nums) - 1 - i):
                        if nums[j] > nums[j + 1]:
                            self.play(bars[j].animate.set_color("#FF0000"), bars[j+1].animate.set_color("#FF0000"), run_time=0.3)
                            self.play(
                                bars[j].animate.shift(RIGHT * 0.8),
                                bars[j+1].animate.shift(LEFT * 0.8),
                                labels[j].animate.shift(RIGHT * 0.8),
                                labels[j+1].animate.shift(LEFT * 0.8),
                                run_time=0.5
                            )
                            bars[j], bars[j+1] = bars[j+1], bars[j]
                            labels[j], labels[j+1] = labels[j+1], labels[j]
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                            self.play(bars[j].animate.set_color("#0066FF"), bars[j+1].animate.set_color("#0066FF"), run_time=0.2)
            
            def _create_math_animation(self, prompt):
                """Create mathematical animation"""
                axes = Axes(x_range=[-3, 3, 1], y_range=[-2, 2, 1], x_length=6, y_length=4, axis_config={"color": "#FFFFFF"})
                self.play(Create(axes))
                
                if 'sine' in prompt.lower():
                    func = axes.plot(lambda x: np.sin(x), color="#FFFF00")
                    label = MathTex(r"y = \sin(x)", color="#FFFF00").to_corner(UR)
                elif 'cosine' in prompt.lower():
                    func = axes.plot(lambda x: np.cos(x), color="#00FF00")
                    label = MathTex(r"y = \cos(x)", color="#00FF00").to_corner(UR)
                elif 'quadratic' in prompt.lower() or 'parabola' in prompt.lower():
                    func = axes.plot(lambda x: x**2, color="#FF0000")
                    label = MathTex(r"y = x^2", color="#FF0000").to_corner(UR)
                else:
                    func = axes.plot(lambda x: x**2, color="#FF0000")
                    label = MathTex(r"y = x^2", color="#FF0000").to_corner(UR)
                
                self.play(Create(func), Write(label))
            
            def _create_physics_animation(self, prompt):
                """Create physics animation"""
                if 'pendulum' in prompt.lower():
                    pivot = Dot(UP * 2, color="#FFFFFF")
                    string = Line(UP * 2, DOWN * 0.5, color="#FFFFFF")
                    bob = Circle(radius=0.2, color="#FFFF00", fill_opacity=1).move_to(DOWN * 0.5)
                    
                    pendulum = VGroup(pivot, string, bob)
                    self.play(Create(pendulum))
                    
                    self.play(Rotate(pendulum, angle=PI/4, about_point=UP * 2), run_time=1)
                    self.play(Rotate(pendulum, angle=-PI/2, about_point=UP * 2), run_time=2)
                    self.play(Rotate(pendulum, angle=PI/4, about_point=UP * 2), run_time=1)
                elif 'wave' in prompt.lower():
                    axes = Axes(x_range=[0, 4*PI, PI], y_range=[-2, 2, 1], x_length=8, y_length=4, axis_config={"color": "#FFFFFF"})
                    self.play(Create(axes))
                    wave = axes.plot(lambda x: np.sin(x), color="#00FFFF")
                    self.play(Create(wave))
                    
                    # Animate wave propagation
                    for i in range(3):
                        new_wave = axes.plot(lambda x: np.sin(x + i*PI/2), color="#00FFFF")
                        self.play(Transform(wave, new_wave), run_time=1)
                else:
                    # Force diagram
                    box = Square(side_length=1, color="#0066FF", fill_opacity=0.5)
                    force_arrow = Arrow(box.get_right(), box.get_right() + RIGHT * 2, color="#FF0000")
                    force_label = Text("F", color="#FF0000", font_size=24).next_to(force_arrow, UP)
                    
                    self.play(Create(box))
                    self.play(Create(force_arrow), Write(force_label))
                    self.play(box.animate.shift(RIGHT * 2), run_time=2)
            
            def _create_data_structure_animation(self, prompt):
                """Create data structure animation"""
                if 'tree' in prompt.lower():
                    nodes = [Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8) for _ in range(3)]
                    labels = [Text(str(i+1), font_size=16, color="#000000") for i in range(3)]
                    
                    nodes[0].shift(UP * 1.5)
                    nodes[1].shift(LEFT * 1.5 + UP * 0.5)
                    nodes[2].shift(RIGHT * 1.5 + UP * 0.5)
                    
                    for i, (node, label) in enumerate(zip(nodes, labels)):
                        label.move_to(node.get_center())
                        self.play(Create(node), Write(label), run_time=0.5)
                        
                    edges = [
                        Line(nodes[0].get_bottom(), nodes[1].get_top(), color="#FFFFFF"),
                        Line(nodes[0].get_bottom(), nodes[2].get_top(), color="#FFFFFF")
                    ]
                    self.play(*[Create(edge) for edge in edges])
                elif 'stack' in prompt.lower():
                    # Stack visualization
                    boxes = VGroup()
                    for i in range(4):
                        box = Rectangle(width=2, height=0.5, color="#0066FF", fill_opacity=0.7)
                        box.shift(DOWN * 2 + UP * i * 0.6)
                        label = Text(f"Item {i+1}", font_size=14, color="#FFFFFF").move_to(box.get_center())
                        boxes.add(VGroup(box, label))
                    
                    # Animate stack operations
                    for i, box_group in enumerate(boxes):
                        self.play(Create(box_group), run_time=0.5)
                        self.wait(0.3)
                else:
                    # Linked list
                    nodes = [Rectangle(width=1, height=0.5, color="#0066FF", fill_opacity=0.7) for _ in range(3)]
                    arrows = [Arrow(ORIGIN, RIGHT * 0.5, color="#FFFFFF") for _ in range(2)]
                    
                    for i, node in enumerate(nodes):
                        node.shift(LEFT * 1 + RIGHT * i * 1.5)
                        if i < 2:
                            arrows[i].next_to(node, RIGHT, buff=0.1)
                    
                    for node, arrow in zip(nodes[:-1], arrows):
                        self.play(Create(node), Create(arrow), run_time=0.5)
                    self.play(Create(nodes[-1]))
            
            def _create_algorithm_animation(self, prompt):
                """Create algorithm animation"""
                if 'search' in prompt.lower():
                    arr = [1, 3, 5, 7, 9, 11, 13]
                    boxes = VGroup()
                    
                    for i, val in enumerate(arr):
                        box = Square(side_length=0.6, color="#0066FF", fill_opacity=0.3)
                        box.shift(LEFT * 3 + RIGHT * i * 0.7)
                        label = Text(str(val), font_size=14, color="#FFFFFF").move_to(box.get_center())
                        boxes.add(VGroup(box, label))
                    
                    self.play(Create(boxes))
                    
                    target = Text("Target: 7", color="#FFFF00", font_size=20).to_edge(UP)
                    self.play(Write(target))
                    
                    # Binary search simulation
                    search_indices = [3, 2, 3]  # Example search path
                    for idx in search_indices:
                        self.play(boxes[idx][0].animate.set_color("#FF0000"), run_time=0.5)
                        self.wait(0.5)
                        final_color = "#00FF00" if arr[idx] == 7 else "#0066FF"
                        self.play(boxes[idx][0].animate.set_color(final_color), run_time=0.5)
                else:
                    # Graph traversal
                    vertices = [Circle(radius=0.3, color="#FFFFFF", fill_opacity=0.8) for _ in range(4)]
                    positions = [UP*1.5, LEFT*1.5, RIGHT*1.5, DOWN*1.5]
                    
                    for i, (vertex, pos) in enumerate(zip(vertices, positions)):
                        vertex.shift(pos)
                        label = Text(str(i+1), font_size=16, color="#000000").move_to(vertex.get_center())
                        self.play(Create(vertex), Write(label), run_time=0.3)
                    
                    # Add edges
                    edges = [
                        Line(vertices[0].get_center(), vertices[1].get_center(), color="#FFFFFF"),
                        Line(vertices[0].get_center(), vertices[2].get_center(), color="#FFFFFF"),
                        Line(vertices[1].get_center(), vertices[3].get_center(), color="#FFFFFF")
                    ]
                    self.play(*[Create(edge) for edge in edges])
            
            def _create_general_animation(self, prompt):
                """Create general animation for any prompt"""
                words = prompt.lower().split()
                
                explanation = Text("Visualizing:", font_size=20, color="#00FFFF").shift(UP * 1)
                self.play(Write(explanation))
                
                # Create shape based on prompt content
                if any(word in words for word in ['circle', 'round', 'ball', 'sphere']):
                    shape = Circle(radius=1, color="#0066FF", fill_opacity=0.5)
                    shape_name = "Circle"
                elif any(word in words for word in ['square', 'box', 'rectangle', 'cube']):
                    shape = Square(side_length=1.5, color="#00FF00", fill_opacity=0.5)
                    shape_name = "Square"
                elif any(word in words for word in ['triangle', 'pyramid']):
                    shape = Triangle(color="#FF0000", fill_opacity=0.5)
                    shape_name = "Triangle"
                elif any(word in words for word in ['star', 'asterisk']):
                    shape = Star(color="#FFFF00", fill_opacity=0.7)
                    shape_name = "Star"
                elif any(word in words for word in ['line', 'arrow', 'vector']):
                    shape = Arrow(LEFT*2, RIGHT*2, color="#FF00FF")
                    shape_name = "Arrow"
                elif any(word in words for word in ['dna', 'helix', 'spiral']):
                    # Create DNA-like double helix
                    helix1 = ParametricFunction(lambda t: np.array([t, np.sin(t), 0]), t_range=[-2*PI, 2*PI], color="#FF0000")
                    helix2 = ParametricFunction(lambda t: np.array([t, -np.sin(t), 0]), t_range=[-2*PI, 2*PI], color="#0000FF")
                    shape = VGroup(helix1, helix2)
                    shape_name = "DNA Helix"
                elif any(word in words for word in ['molecule', 'atom', 'chemistry']):
                    # Create molecular structure
                    center = Circle(radius=0.3, color="#FFFF00", fill_opacity=1)
                    electrons = [Circle(radius=0.1, color="#0066FF", fill_opacity=1) for _ in range(3)]
                    for i, electron in enumerate(electrons):
                        angle = i * 2 * PI / 3
                        electron.shift(1.5 * np.cos(angle) * RIGHT + 1.5 * np.sin(angle) * UP)
                    shape = VGroup(center, *electrons)
                    shape_name = "Molecule"
                elif any(word in words for word in ['cell', 'biology', 'mitosis']):
                    # Create cell-like structure
                    cell_wall = Circle(radius=1.5, color="#00FF00", fill_opacity=0.2)
                    nucleus = Circle(radius=0.5, color="#FF0000", fill_opacity=0.5)
                    shape = VGroup(cell_wall, nucleus)
                    shape_name = "Cell"
                else:
                    # Default: animated text with geometric pattern
                    shape = RegularPolygon(n=6, color="#FFFF00", fill_opacity=0.7)
                    shape_name = "Hexagon"
                
                self.play(Create(shape))
                
                # Add animations based on prompt content
                if any(word in words for word in ['rotate', 'spin', 'turn']):
                    self.play(Rotate(shape, angle=2*PI), run_time=2)
                elif any(word in words for word in ['grow', 'expand', 'scale']):
                    self.play(shape.animate.scale(2), run_time=1.5)
                    self.play(shape.animate.scale(0.5), run_time=1.5)
                elif any(word in words for word in ['move', 'translate', 'shift']):
                    self.play(shape.animate.shift(RIGHT * 2), run_time=1)
                    self.play(shape.animate.shift(LEFT * 4), run_time=1)
                    self.play(shape.animate.shift(RIGHT * 2), run_time=1)
                elif any(word in words for word in ['pulse', 'beat', 'oscillate']):
                    for _ in range(3):
                        self.play(shape.animate.scale(1.3), run_time=0.5)
                        self.play(shape.animate.scale(1/1.3), run_time=0.5)
                else:
                    # Default animation sequence
                    self.play(shape.animate.scale(1.5), run_time=1)
                    self.play(Rotate(shape, angle=PI), run_time=1.5)
                    self.play(shape.animate.scale(0.7), run_time=1)
                
                # Add descriptive text
                desc = Text(f"{shape_name}: {prompt[:25]}..." if len(prompt) > 25 else f"{shape_name}: {prompt}", 
                           font_size=16, color="#FFFFFF").shift(DOWN * 2)
                self.play(Write(desc))
        
        return DynamicScene
    
    def _render_scene(self, scene_class, animation_id: str) -> str:
        """Render the Manim scene and return video path"""
        
        # Configure Manim for web output
        config.media_dir = self.output_dir
        config.video_dir = os.path.join(self.output_dir, "videos")
        config.quality = "medium_quality"
        config.format = "mp4"
        config.frame_rate = 30
        config.background_color = "#000000"
        
        # Create and render scene
        scene = scene_class()
        scene.render()
        
        # Find the generated video file
        video_files = []
        for root, dirs, files in os.walk(config.video_dir):
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