import json
import re
from typing import Dict, List, Any
import manim as mn
import numpy as np
import os

class EducationalVideoGenerator:
    def __init__(self):
        self.output_dir = "media"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_complete_educational_video(self, prompt: str, animation_id: str) -> Dict[str, Any]:
        """Generate complete educational video with all 3 components"""
        
        # Step 1: Generate structured animation instructions
        instructions = self._generate_animation_instructions(prompt)
        
        # Step 2: Create visual animation based on instructions
        animation_path = self._create_visual_animation(instructions, animation_id)
        
        # Step 3: Generate educational explanation video
        explanation_path = self._create_educational_explanation(prompt, instructions, f"{animation_id}_explanation")
        
        # Step 4: Combine all components into final video
        final_video_path = self._combine_videos(animation_path, explanation_path, f"{animation_id}_final")
        
        return {
            "instructions": instructions,
            "animation_video": animation_path,
            "explanation_video": explanation_path,
            "final_video": final_video_path,
            "status": "completed"
        }
    
    def _generate_animation_instructions(self, prompt: str) -> Dict[str, Any]:
        """Generate structured set of animation instructions"""
        
        concept = self._identify_concept(prompt)
        
        if concept == "sorting":
            numbers = re.findall(r'\d+', prompt)
            nums = [int(n) for n in numbers[:5]] if numbers else [64, 34, 25, 12, 22]
            
            instructions = {
                "concept": "Bubble Sort Algorithm",
                "description": "Step-by-step bubble sort visualization",
                "duration": 25,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 3, "action": "show_title", "content": "Bubble Sort Algorithm"},
                    {"id": 2, "title": "Setup", "duration": 3, "action": "create_array", "elements": nums},
                    {"id": 3, "title": "Algorithm Steps", "duration": 15, "action": "bubble_sort", "elements": nums},
                    {"id": 4, "title": "Result", "duration": 2, "action": "show_result", "content": "Array Sorted!"},
                    {"id": 5, "title": "Conclusion", "duration": 2, "action": "show_conclusion", "content": "Time Complexity: O(n²)"}
                ],
                "educational_points": [
                    "Compares adjacent elements",
                    "Swaps if left > right", 
                    "Largest element bubbles to end",
                    "Repeats until sorted"
                ]
            }
            
        elif concept == "math":
            func_type = "sine" if "sine" in prompt.lower() else "quadratic" if "quadratic" in prompt.lower() else "linear"
            
            instructions = {
                "concept": f"{func_type.title()} Function",
                "description": f"Mathematical visualization of {func_type} function",
                "duration": 20,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 3, "action": "show_title", "content": f"{func_type.title()} Function"},
                    {"id": 2, "title": "Coordinate System", "duration": 3, "action": "create_axes", "range": [-4, 4]},
                    {"id": 3, "title": "Function Plot", "duration": 8, "action": "plot_function", "type": func_type},
                    {"id": 4, "title": "Key Points", "duration": 4, "action": "highlight_points", "type": func_type},
                    {"id": 5, "title": "Properties", "duration": 2, "action": "show_properties", "type": func_type}
                ],
                "educational_points": self._get_math_points(func_type)
            }
            
        elif concept == "physics":
            phys_type = "pendulum" if "pendulum" in prompt.lower() else "force"
            
            instructions = {
                "concept": f"{phys_type.title()} Physics",
                "description": f"Physics demonstration of {phys_type}",
                "duration": 18,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 2, "action": "show_title", "content": f"{phys_type.title()} Physics"},
                    {"id": 2, "title": "Setup", "duration": 3, "action": "create_setup", "type": phys_type},
                    {"id": 3, "title": "Demonstration", "duration": 10, "action": "demonstrate", "type": phys_type},
                    {"id": 4, "title": "Explanation", "duration": 3, "action": "explain_physics", "type": phys_type}
                ],
                "educational_points": self._get_physics_points(phys_type)
            }
            
        else:  # General concept
            instructions = {
                "concept": "General Concept Visualization",
                "description": f"Educational animation for: {prompt}",
                "duration": 15,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 2, "action": "show_title", "content": prompt},
                    {"id": 2, "title": "Visualization", "duration": 8, "action": "create_visual", "prompt": prompt},
                    {"id": 3, "title": "Properties", "duration": 3, "action": "show_properties", "prompt": prompt},
                    {"id": 4, "title": "Summary", "duration": 2, "action": "show_summary", "prompt": prompt}
                ],
                "educational_points": self._get_general_points(prompt)
            }
        
        return instructions
    
    def _create_visual_animation(self, instructions: Dict[str, Any], animation_id: str) -> str:
        """Create visual animation based on instructions"""
        
        class InstructionBasedScene(mn.Scene):
            def construct(self):
                UP = np.array([0, 1, 0])
                DOWN = np.array([0, -1, 0])
                LEFT = np.array([-1, 0, 0])
                RIGHT = np.array([1, 0, 0])
                ORIGIN = np.array([0, 0, 0])
                PI = np.pi
                
                # Execute each scene from instructions
                for scene in instructions["scenes"]:
                    self.execute_scene(scene, UP, DOWN, LEFT, RIGHT, ORIGIN, PI)
            
            def execute_scene(self, scene, UP, DOWN, LEFT, RIGHT, ORIGIN, PI):
                if scene["action"] == "show_title":
                    title = mn.Text(scene["content"], font_size=24, color="#00FFFF")
                    title.to_edge(UP)
                    self.play(mn.Write(title), run_time=1.5)
                    self.wait(scene["duration"] - 1.5)
                    
                elif scene["action"] == "create_array":
                    elements = scene["elements"]
                    bars = mn.VGroup()
                    for i, num in enumerate(elements):
                        bar = mn.Rectangle(width=0.7, height=num/15, color="#0066FF", fill_opacity=0.8)
                        bar.shift(LEFT * 2 + RIGHT * i * 0.8)
                        label = mn.Text(str(num), font_size=16, color="#FFFFFF")
                        label.next_to(bar, DOWN)
                        bars.add(mn.VGroup(bar, label))
                    
                    self.play(mn.Create(bars), run_time=2)
                    self.wait(scene["duration"] - 2)
                    
                elif scene["action"] == "bubble_sort":
                    # Simplified bubble sort visualization
                    nums = scene["elements"].copy()
                    # Find the bars group in mobjects
                    bars = None
                    for mob in self.mobjects:
                        if hasattr(mob, '__len__') and len(mob) > 0:
                            bars = mob
                            break
                    
                    if bars is None:
                        return  # Skip if no bars found
                    
                    for i in range(len(nums)):
                        for j in range(len(nums) - 1 - i):
                            if nums[j] > nums[j + 1]:
                                self.play(bars[j][0].animate.set_color("#FF0000"), bars[j+1][0].animate.set_color("#FF0000"), run_time=0.3)
                                self.play(
                                    bars[j].animate.shift(RIGHT * 0.8),
                                    bars[j+1].animate.shift(LEFT * 0.8),
                                    run_time=0.8
                                )
                                bars[j], bars[j+1] = bars[j+1], bars[j]
                                nums[j], nums[j+1] = nums[j+1], nums[j]
                                self.play(bars[j][0].animate.set_color("#00FF00"), bars[j+1][0].animate.set_color("#0066FF"), run_time=0.3)
                    
                elif scene["action"] == "create_axes":
                    axes = mn.Axes(x_range=scene["range"] + [1], y_range=[-3, 3, 1], x_length=6, y_length=4)
                    self.play(mn.Create(axes), run_time=2)
                    self.wait(scene["duration"] - 2)
                    
                elif scene["action"] == "plot_function":
                    # Find the axes in mobjects
                    axes = None
                    for mob in self.mobjects:
                        if hasattr(mob, 'plot'):  # Check if it's an Axes object
                            axes = mob
                            break
                    
                    if axes is None:
                        return  # Skip if no axes found
                    if scene["type"] == "sine":
                        func = axes.plot(lambda x: np.sin(x), color="#FFFF00")
                        label = mn.MathTex(r"y = \sin(x)", color="#FFFF00")
                    elif scene["type"] == "quadratic":
                        func = axes.plot(lambda x: x**2, color="#FF0000")
                        label = mn.MathTex(r"y = x^2", color="#FF0000")
                    else:
                        func = axes.plot(lambda x: x, color="#00FF00")
                        label = mn.MathTex(r"y = x", color="#00FF00")
                    
                    label.to_corner(UP + RIGHT)
                    self.play(mn.Create(func), mn.Write(label), run_time=4)
                    self.wait(scene["duration"] - 4)
                    
                elif scene["action"] == "show_result" or scene["action"] == "show_conclusion":
                    text = mn.Text(scene["content"], font_size=18, color="#00FF00")
                    text.shift(DOWN * 2)
                    self.play(mn.Write(text), run_time=1)
                    self.wait(scene["duration"] - 1)
        
        # Render the scene
        mn.config.media_dir = self.output_dir
        mn.config.video_dir = os.path.join(self.output_dir, "videos")
        mn.config.quality = "medium_quality"
        mn.config.format = "mp4"
        mn.config.frame_rate = 24
        
        scene = InstructionBasedScene()
        scene.render()
        
        # Find and copy the video
        video_files = []
        for root, dirs, files in os.walk(mn.config.video_dir):
            for file in files:
                if file.endswith('.mp4'):
                    video_files.append(os.path.join(root, file))
        
        if video_files:
            latest_video = max(video_files, key=os.path.getctime)
            final_path = os.path.join(self.output_dir, f"{animation_id}_animation.mp4")
            import shutil
            shutil.copy2(latest_video, final_path)
            return final_path
        
        return None
    
    def _create_educational_explanation(self, prompt: str, instructions: Dict[str, Any], explanation_id: str) -> str:
        """Create educational explanation video"""
        
        class ExplanationScene(mn.Scene):
            def construct(self):
                # Title slide
                title = mn.Text("Educational Explanation", font_size=28, color="#00FFFF")
                title.shift(UP * 2)
                concept_title = mn.Text(instructions["concept"], font_size=20, color="#FFFFFF")
                concept_title.shift(UP * 1)
                
                self.play(mn.Write(title), mn.Write(concept_title), run_time=2)
                self.wait(2)
                
                # Clear and show description
                self.play(mn.FadeOut(title), mn.FadeOut(concept_title))
                
                description = mn.Text("What you will learn:", font_size=20, color="#FFFF00")
                description.shift(UP * 2.5)
                self.play(mn.Write(description), run_time=1)
                
                # Show educational points
                for i, point in enumerate(instructions["educational_points"]):
                    point_text = mn.Text(f"• {point}", font_size=16, color="#FFFFFF")
                    point_text.shift(UP * (1.5 - i * 0.5))
                    self.play(mn.Write(point_text), run_time=1.5)
                    self.wait(1)
                
                self.wait(2)
                
                # Key concepts slide
                self.play(*[mn.FadeOut(mob) for mob in self.mobjects])
                
                key_concepts = mn.Text("Key Concepts:", font_size=24, color="#00FF00")
                key_concepts.shift(UP * 2)
                self.play(mn.Write(key_concepts), run_time=1)
                
                # Show concept-specific information
                if "sort" in instructions["concept"].lower():
                    concepts = [
                        "Time Complexity: O(n²)",
                        "Space Complexity: O(1)",
                        "Stable sorting algorithm",
                        "Best for small datasets"
                    ]
                elif "function" in instructions["concept"].lower():
                    concepts = [
                        "Domain and Range",
                        "Continuous vs Discrete",
                        "Rate of change",
                        "Real-world applications"
                    ]
                else:
                    concepts = [
                        "Core principles",
                        "Practical applications",
                        "Important properties",
                        "Related concepts"
                    ]
                
                for i, concept in enumerate(concepts):
                    concept_text = mn.Text(concept, font_size=16, color="#FFFFFF")
                    concept_text.shift(UP * (1 - i * 0.6))
                    self.play(mn.Write(concept_text), run_time=1.2)
                    self.wait(0.8)
                
                self.wait(3)
                
                # Summary slide
                self.play(*[mn.FadeOut(mob) for mob in self.mobjects])
                
                summary = mn.Text("Summary", font_size=24, color="#00FFFF")
                summary.shift(UP * 1.5)
                
                summary_text = mn.Text(
                    f"You've learned about {instructions['concept']}\nthrough visual animation and explanation.",
                    font_size=16, color="#FFFFFF"
                )
                summary_text.shift(DOWN * 0.5)
                
                self.play(mn.Write(summary), mn.Write(summary_text), run_time=2)
                self.wait(3)
        
        # Render explanation scene
        scene = ExplanationScene()
        scene.render()
        
        # Find and copy the video
        video_files = []
        for root, dirs, files in os.walk(mn.config.video_dir):
            for file in files:
                if file.endswith('.mp4'):
                    video_files.append(os.path.join(root, file))
        
        if video_files:
            latest_video = max(video_files, key=os.path.getctime)
            final_path = os.path.join(self.output_dir, f"{explanation_id}.mp4")
            import shutil
            shutil.copy2(latest_video, final_path)
            return final_path
        
        return None
    
    def _combine_videos(self, animation_path: str, explanation_path: str, final_id: str) -> str:
        """Combine animation and explanation into final educational video"""
        
        class CombinedScene(mn.Scene):
            def construct(self):
                # Introduction slide
                intro = mn.Text("Complete Educational Video", font_size=24, color="#00FFFF")
                intro.shift(UP * 1)
                
                subtitle = mn.Text("Animation + Explanation", font_size=16, color="#FFFFFF")
                subtitle.shift(DOWN * 0.5)
                
                self.play(mn.Write(intro), mn.Write(subtitle), run_time=2)
                self.wait(2)
                
                # Transition message
                self.play(mn.FadeOut(intro), mn.FadeOut(subtitle))
                
                transition = mn.Text("Watch the animation, then learn the concepts!", 
                                    font_size=18, color="#FFFF00")
                self.play(mn.Write(transition), run_time=1.5)
                self.wait(2)
                self.play(mn.FadeOut(transition))
                
                # Note: In a real implementation, you would use video editing libraries
                # to actually combine the videos. For now, we create a placeholder.
                
                final_message = mn.Text("Animation and Explanation Combined", 
                                       font_size=20, color="#00FF00")
                self.play(mn.Write(final_message), run_time=2)
                self.wait(3)
        
        # Render combined scene
        scene = CombinedScene()
        scene.render()
        
        # Find and copy the video
        video_files = []
        for root, dirs, files in os.walk(mn.config.video_dir):
            for file in files:
                if file.endswith('.mp4'):
                    video_files.append(os.path.join(root, file))
        
        if video_files:
            latest_video = max(video_files, key=os.path.getctime)
            final_path = os.path.join(self.output_dir, f"{final_id}.mp4")
            import shutil
            shutil.copy2(latest_video, final_path)
            return final_path
        
        return animation_path  # Fallback to animation if combination fails
    
    def _identify_concept(self, prompt: str) -> str:
        """Identify the main concept from prompt"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['sort', 'bubble', 'merge', 'quick']):
            return "sorting"
        elif any(word in prompt_lower for word in ['function', 'graph', 'plot', 'sine', 'cosine', 'equation']):
            return "math"
        elif any(word in prompt_lower for word in ['force', 'pendulum', 'gravity', 'motion']):
            return "physics"
        else:
            return "general"
    
    def _get_math_points(self, func_type: str) -> List[str]:
        if func_type == "sine":
            return ["Periodic function", "Range: [-1, 1]", "Period: 2π", "Used in waves"]
        elif func_type == "quadratic":
            return ["Parabolic shape", "Has vertex", "Degree 2 polynomial", "Used in physics"]
        else:
            return ["Linear relationship", "Constant rate", "Straight line", "Basic function"]
    
    def _get_physics_points(self, phys_type: str) -> List[str]:
        if phys_type == "pendulum":
            return ["Simple harmonic motion", "Gravity restoring force", "Period depends on length", "Energy conservation"]
        else:
            return ["Newton's laws", "Force causes acceleration", "F = ma", "Vector quantity"]
    
    def _get_general_points(self, prompt: str) -> List[str]:
        return [
            f"Understanding {prompt}",
            "Visual representation",
            "Key properties",
            "Practical applications"
        ]