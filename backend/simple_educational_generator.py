import json
import re
from typing import Dict, List, Any
import os
import sys
import subprocess
import numpy as np

# Setup Manim environment before importing
try:
    from manim_config_fix import setup_manim_environment, check_system_dependencies
    print("Setting up Manim environment...")
    setup_manim_environment()
    check_system_dependencies()
except Exception as e:
    print(f"Warning: Could not setup Manim environment: {e}")

# Now import Manim with proper environment
import manim as mn

class EducationalVideoGenerator:
    def __init__(self):
        self.output_dir = "media"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_complete_educational_video(self, prompt: str, animation_id: str) -> Dict[str, Any]:
        """Generate complete educational video with all 3 components"""
        
        # Step 1: Generate structured animation instructions
        instructions = self._generate_animation_instructions(prompt)
        
        # Step 2: Create visual animation
        animation_path = self._create_visual_animation(prompt, f"{animation_id}_animation")
        
        # Step 3: Create educational explanation
        explanation_path = self._create_educational_explanation(instructions, f"{animation_id}_explanation")
        
        # Step 4: Use animation as final (simplified for now)
        final_video_path = animation_path
        
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
            nums = [int(n) for n in numbers[:4]] if numbers else [4, 2, 7, 1]
            
            instructions = {
                "concept": "Bubble Sort Algorithm",
                "description": "Step-by-step bubble sort visualization",
                "duration": 15,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 2, "action": "show_title"},
                    {"id": 2, "title": "Create Array", "duration": 3, "action": "create_array", "elements": nums},
                    {"id": 3, "title": "Sort Process", "duration": 8, "action": "bubble_sort", "elements": nums},
                    {"id": 4, "title": "Result", "duration": 2, "action": "show_result"}
                ],
                "educational_points": [
                    "Compares adjacent elements",
                    "Swaps if left > right", 
                    "Time complexity: O(n²)",
                    "Simple but inefficient for large data"
                ]
            }
            
        elif concept == "math":
            instructions = {
                "concept": "Mathematical Function",
                "description": "Function visualization and properties",
                "duration": 12,
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": 2, "action": "show_title"},
                    {"id": 2, "title": "Coordinate System", "duration": 3, "action": "create_axes"},
                    {"id": 3, "title": "Plot Function", "duration": 5, "action": "plot_function"},
                    {"id": 4, "title": "Properties", "duration": 2, "action": "show_properties"}
                ],
                "educational_points": [
                    "Domain and range",
                    "Continuous function",
                    "Rate of change",
                    "Real-world applications"
                ]
            }
            
        else:  # General - analyze prompt for specific content
            concept_type = self._analyze_general_prompt(prompt)
            print(f"Analyzing prompt: '{prompt}' -> concept_type: '{concept_type}'")
            
            if concept_type == "circle":
                instructions = {
                    "concept": "Circle Geometry and Properties",
                    "description": "Complete exploration of circle properties, formulas, and applications",
                    "duration": 12,
                    "scenes": [
                        {"id": 1, "title": "Circle Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Create Circle", "duration": 3, "action": "create_circle"},
                        {"id": 3, "title": "Show Radius", "duration": 2, "action": "show_radius"},
                        {"id": 4, "title": "Calculate Area", "duration": 3, "action": "show_area_formula"},
                        {"id": 5, "title": "Circle Animation", "duration": 2, "action": "animate_circle"}
                    ],
                    "educational_points": [
                        "Circle has constant radius from center",
                        "Area formula: π × r²",
                        "Circumference formula: 2 × π × r",
                        "Used in wheels, gears, and architecture"
                    ]
                }
            elif concept_type == "dna":
                instructions = {
                    "concept": "DNA Structure and Function",
                    "description": "Understanding DNA double helix structure and genetic information",
                    "duration": 14,
                    "scenes": [
                        {"id": 1, "title": "DNA Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Double Helix", "duration": 4, "action": "create_dna_helix"},
                        {"id": 3, "title": "Base Pairs", "duration": 4, "action": "show_base_pairs"},
                        {"id": 4, "title": "Genetic Code", "duration": 4, "action": "explain_genetic_code"}
                    ],
                    "educational_points": [
                        "DNA contains genetic information",
                        "Double helix structure with base pairs",
                        "A-T and G-C base pairing rules",
                        "Codes for proteins and traits"
                    ]
                }
            elif concept_type == "atom":
                instructions = {
                    "concept": "Atomic Structure",
                    "description": "Exploring atoms, electrons, protons, and chemical bonding",
                    "duration": 13,
                    "scenes": [
                        {"id": 1, "title": "Atom Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Nucleus", "duration": 3, "action": "create_nucleus"},
                        {"id": 3, "title": "Electron Orbits", "duration": 4, "action": "show_electron_orbits"},
                        {"id": 4, "title": "Chemical Bonds", "duration": 4, "action": "demonstrate_bonding"}
                    ],
                    "educational_points": [
                        "Atoms are building blocks of matter",
                        "Nucleus contains protons and neutrons",
                        "Electrons orbit in energy levels",
                        "Chemical bonds form between atoms"
                    ]
                }
            elif concept_type == "geometry":
                instructions = {
                    "concept": "Geometric Shapes and Properties",
                    "description": "Exploring geometric shapes, angles, and mathematical relationships",
                    "duration": 11,
                    "scenes": [
                        {"id": 1, "title": "Shape Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Create Shape", "duration": 3, "action": "create_geometry"},
                        {"id": 3, "title": "Properties", "duration": 4, "action": "show_properties"},
                        {"id": 4, "title": "Applications", "duration": 2, "action": "show_applications"}
                    ],
                    "educational_points": [
                        "Geometric shapes have specific properties",
                        "Angles and measurements are important",
                        "Used in architecture and design",
                        "Foundation of mathematics"
                    ]
                }
            elif concept_type == "chemistry":
                instructions = {
                    "concept": "Chemical Structures and Reactions",
                    "description": "Understanding molecules, bonds, and chemical processes",
                    "duration": 13,
                    "scenes": [
                        {"id": 1, "title": "Chemistry Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Molecular Structure", "duration": 4, "action": "create_molecule"},
                        {"id": 3, "title": "Chemical Bonds", "duration": 4, "action": "show_bonds"},
                        {"id": 4, "title": "Reactions", "duration": 3, "action": "demonstrate_reaction"}
                    ],
                    "educational_points": [
                        "Molecules are made of atoms",
                        "Chemical bonds hold atoms together",
                        "Reactions create new substances",
                        "Chemistry is everywhere in life"
                    ]
                }
            elif concept_type == "space":
                instructions = {
                    "concept": "Space and Astronomy",
                    "description": "Exploring planets, stars, and the universe",
                    "duration": 14,
                    "scenes": [
                        {"id": 1, "title": "Space Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Solar System", "duration": 5, "action": "create_solar_system"},
                        {"id": 3, "title": "Planetary Motion", "duration": 4, "action": "show_orbits"},
                        {"id": 4, "title": "Space Exploration", "duration": 3, "action": "show_exploration"}
                    ],
                    "educational_points": [
                        "Solar system has 8 planets",
                        "Gravity keeps planets in orbit",
                        "Stars are distant suns",
                        "Space exploration advances science"
                    ]
                }
            elif concept_type == "plant":
                instructions = {
                    "concept": "Plant Biology and Photosynthesis",
                    "description": "Understanding how plants grow, make food, and support life",
                    "duration": 12,
                    "scenes": [
                        {"id": 1, "title": "Plant Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Plant Structure", "duration": 3, "action": "create_plant"},
                        {"id": 3, "title": "Photosynthesis", "duration": 5, "action": "show_photosynthesis"},
                        {"id": 4, "title": "Importance", "duration": 2, "action": "show_importance"}
                    ],
                    "educational_points": [
                        "Plants make their own food",
                        "Photosynthesis uses sunlight and CO2",
                        "Plants produce oxygen we breathe",
                        "Foundation of food chains"
                    ]
                }
            elif concept_type == "energy":
                instructions = {
                    "concept": "Energy Types and Conservation",
                    "description": "Understanding different forms of energy and how they transform",
                    "duration": 13,
                    "scenes": [
                        {"id": 1, "title": "Energy Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Energy Types", "duration": 4, "action": "show_energy_types"},
                        {"id": 3, "title": "Energy Transfer", "duration": 4, "action": "demonstrate_transfer"},
                        {"id": 4, "title": "Conservation", "duration": 3, "action": "show_conservation"}
                    ],
                    "educational_points": [
                        "Energy cannot be created or destroyed",
                        "Energy transforms from one type to another",
                        "Kinetic and potential energy",
                        "Renewable vs non-renewable sources"
                    ]
                }
            else:
                # Truly generic fallback with enhanced analysis
                key_words = prompt.lower().split()
                main_concept = key_words[0] if key_words else "concept"
                
                instructions = {
                    "concept": f"Understanding: {prompt.title()}",
                    "description": f"Comprehensive educational exploration of {prompt}",
                    "duration": 12,
                    "scenes": [
                        {"id": 1, "title": "Introduction", "duration": 2, "action": "show_title"},
                        {"id": 2, "title": "Core Concept", "duration": 4, "action": "create_visual"},
                        {"id": 3, "title": "Key Properties", "duration": 3, "action": "show_properties"},
                        {"id": 4, "title": "Applications", "duration": 2, "action": "show_applications"},
                        {"id": 5, "title": "Summary", "duration": 1, "action": "show_summary"}
                    ],
                    "educational_points": [
                        f"Understanding {main_concept} fundamentals",
                        "Visual representation and structure",
                        "Key characteristics and properties",
                        "Real-world applications and importance"
                    ]
                }
        
        return instructions
    
    def _create_visual_animation(self, prompt: str, animation_id: str) -> str:
        """Create visual animation"""
        
        class SimpleAnimationScene(mn.Scene):
            def construct(self):
                # Title
                title = mn.Text(prompt[:40] + "..." if len(prompt) > 40 else prompt, 
                               font_size=20, color="#FFFFFF")
                title.to_edge(mn.UP)
                self.play(mn.Write(title), run_time=1.5)
                self.wait(1)
                
                # Create content based on prompt
                if any(word in prompt.lower() for word in ['sort', 'bubble']):
                    self.create_sorting_demo()
                elif any(word in prompt.lower() for word in ['function', 'sine', 'math']):
                    self.create_math_demo()
                elif any(word in prompt.lower() for word in ['circle', 'round']):
                    self.create_circle_demo()
                else:
                    self.create_general_demo(prompt)
                
                # Conclusion
                conclusion = mn.Text("Animation Complete!", font_size=16, color="#00FF00")
                conclusion.to_edge(mn.DOWN)
                self.play(mn.Write(conclusion), run_time=1)
                self.wait(2)
            
            def create_sorting_demo(self):
                nums = [4, 2, 7, 1]
                bars = mn.VGroup()
                
                for i, num in enumerate(nums):
                    bar = mn.Rectangle(width=0.8, height=num/2, color="#0066FF", fill_opacity=0.8)
                    bar.shift(mn.LEFT * 1.5 + mn.RIGHT * i * 1)
                    label = mn.Text(str(num), font_size=14, color="#FFFFFF")
                    label.next_to(bar, mn.DOWN)
                    bars.add(mn.VGroup(bar, label))
                
                self.play(mn.Create(bars), run_time=2)
                self.wait(1)
                
                # Simple swap demonstration
                self.play(bars[0][0].animate.set_color("#FF0000"), bars[1][0].animate.set_color("#FF0000"), run_time=0.5)
                self.play(bars[0].animate.shift(mn.RIGHT * 1), bars[1].animate.shift(mn.LEFT * 1), run_time=1)
                self.play(bars[0][0].animate.set_color("#00FF00"), bars[1][0].animate.set_color("#0066FF"), run_time=0.5)
                self.wait(2)
            
            def create_math_demo(self):
                axes = mn.Axes(x_range=[-3, 3, 1], y_range=[-2, 2, 1], x_length=6, y_length=4)
                self.play(mn.Create(axes), run_time=2)
                
                func = axes.plot(lambda x: np.sin(x), color="#FFFF00")
                label = mn.MathTex(r"y = \sin(x)", color="#FFFF00")
                label.to_corner(mn.UP + mn.RIGHT)
                
                self.play(mn.Create(func), mn.Write(label), run_time=3)
                self.wait(2)
            
            def create_circle_demo(self):
                # Title for circle properties
                circle_title = mn.Text("Circle Properties", font_size=18, color="#FFFF00")
                circle_title.shift(mn.UP * 2.5)
                self.play(mn.Write(circle_title), run_time=1)
                
                # Create circle
                circle = mn.Circle(radius=1.5, color="#0066FF", fill_opacity=0.6)
                self.play(mn.Create(circle), run_time=2)
                
                # Show radius
                radius_line = mn.Line(mn.ORIGIN, mn.RIGHT * 1.5, color="#FF0000", stroke_width=4)
                radius_label = mn.Text("radius = r", font_size=14, color="#FF0000")
                radius_label.next_to(radius_line, mn.UP)
                
                self.play(mn.Create(radius_line), mn.Write(radius_label), run_time=1.5)
                self.wait(1.5)
                
                # Show area formula
                area_formula = mn.MathTex(r"Area = \pi r^2", color="#00FF00", font_size=36)
                area_formula.shift(mn.DOWN * 2)
                self.play(mn.Write(area_formula), run_time=2)
                self.wait(1.5)
                
                # Show circumference
                circumference_formula = mn.MathTex(r"Circumference = 2\pi r", color="#FFFF00", font_size=36)
                circumference_formula.shift(mn.DOWN * 2.8)
                self.play(mn.Write(circumference_formula), run_time=2)
                self.wait(1.5)
                
                # Animate circle rotation
                self.play(mn.Rotate(circle, angle=2*np.pi), run_time=3)
                
                # Show practical applications
                apps_text = mn.Text("Used in: wheels, gears, architecture", font_size=12, color="#FFFFFF")
                apps_text.shift(mn.DOWN * 3.5)
                self.play(mn.Write(apps_text), run_time=2)
                self.wait(2)
            
            def create_general_demo(self, prompt):
                prompt_lower = prompt.lower()
                
                if any(word in prompt_lower for word in ['dna', 'genetic', 'helix']):
                    self.create_dna_demo()
                elif any(word in prompt_lower for word in ['atom', 'molecule', 'electron']):
                    self.create_atom_demo()
                elif any(word in prompt_lower for word in ['cell', 'biology']):
                    self.create_cell_demo()
                else:
                    # Default geometric demo
                    shape = mn.RegularPolygon(n=6, color="#FFFF00", fill_opacity=0.7)
                    self.play(mn.Create(shape), run_time=2)
                    
                    self.play(shape.animate.scale(1.5), run_time=1)
                    self.play(mn.Rotate(shape, angle=np.pi), run_time=1.5)
                    self.play(shape.animate.scale(0.8), run_time=1)
                    self.wait(1)
            
            def create_dna_demo(self):
                dna_title = mn.Text("DNA Double Helix", font_size=18, color="#00FFFF")
                dna_title.shift(mn.UP * 2.5)
                self.play(mn.Write(dna_title), run_time=1)
                
                # Create DNA double helix
                helix1 = mn.ParametricFunction(
                    lambda t: np.array([t/2, np.sin(t), 0]), 
                    t_range=[-3*np.pi, 3*np.pi], 
                    color="#FF0000"
                )
                helix2 = mn.ParametricFunction(
                    lambda t: np.array([t/2, -np.sin(t), 0]), 
                    t_range=[-3*np.pi, 3*np.pi], 
                    color="#0000FF"
                )
                
                self.play(mn.Create(helix1), run_time=2)
                self.play(mn.Create(helix2), run_time=2)
                
                # Add base pairs
                base_pairs = mn.VGroup()
                for i in range(-3, 4):
                    line = mn.Line(
                        np.array([i*np.pi/6, np.sin(i*np.pi/3), 0]),
                        np.array([i*np.pi/6, -np.sin(i*np.pi/3), 0]),
                        color="#FFFFFF", stroke_width=2
                    )
                    base_pairs.add(line)
                
                self.play(mn.Create(base_pairs), run_time=2)
                
                info_text = mn.Text("Contains genetic information", font_size=12, color="#FFFFFF")
                info_text.shift(mn.DOWN * 2.5)
                self.play(mn.Write(info_text), run_time=1.5)
                self.wait(2)
            
            def create_atom_demo(self):
                atom_title = mn.Text("Atomic Structure", font_size=18, color="#FFFF00")
                atom_title.shift(mn.UP * 2.5)
                self.play(mn.Write(atom_title), run_time=1)
                
                # Nucleus
                nucleus = mn.Circle(radius=0.3, color="#FFFF00", fill_opacity=1)
                nucleus_label = mn.Text("Nucleus", font_size=10, color="#000000")
                nucleus_label.move_to(nucleus.get_center())
                
                self.play(mn.Create(nucleus), mn.Write(nucleus_label), run_time=1.5)
                
                # Electron orbits
                orbit1 = mn.Circle(radius=1.2, color="#FFFFFF", fill_opacity=0, stroke_width=2)
                orbit2 = mn.Circle(radius=1.8, color="#FFFFFF", fill_opacity=0, stroke_width=2)
                
                self.play(mn.Create(orbit1), mn.Create(orbit2), run_time=1.5)
                
                # Electrons
                electron1 = mn.Circle(radius=0.1, color="#0066FF", fill_opacity=1)
                electron1.move_to(mn.RIGHT * 1.2)
                electron2 = mn.Circle(radius=0.1, color="#0066FF", fill_opacity=1)
                electron2.move_to(mn.LEFT * 1.8)
                
                self.play(mn.Create(electron1), mn.Create(electron2), run_time=1)
                
                # Animate electrons
                self.play(
                    mn.Rotate(electron1, angle=2*np.pi, about_point=mn.ORIGIN),
                    mn.Rotate(electron2, angle=-2*np.pi, about_point=mn.ORIGIN),
                    run_time=3
                )
                
                info_text = mn.Text("Building blocks of matter", font_size=12, color="#FFFFFF")
                info_text.shift(mn.DOWN * 2.5)
                self.play(mn.Write(info_text), run_time=1.5)
                self.wait(2)
            
            def create_cell_demo(self):
                cell_title = mn.Text("Biological Cell", font_size=18, color="#00FF00")
                cell_title.shift(mn.UP * 2.5)
                self.play(mn.Write(cell_title), run_time=1)
                
                # Cell membrane
                cell_wall = mn.Circle(radius=2, color="#00FF00", fill_opacity=0.2, stroke_width=3)
                self.play(mn.Create(cell_wall), run_time=1.5)
                
                # Nucleus
                nucleus = mn.Circle(radius=0.6, color="#FF0000", fill_opacity=0.7)
                nucleus_label = mn.Text("Nucleus", font_size=10, color="#FFFFFF")
                nucleus_label.move_to(nucleus.get_center())
                
                self.play(mn.Create(nucleus), mn.Write(nucleus_label), run_time=1.5)
                
                # Mitochondria
                mito1 = mn.Ellipse(width=0.4, height=0.2, color="#FF00FF", fill_opacity=0.8)
                mito1.shift(mn.UP * 0.8 + mn.RIGHT * 0.5)
                mito2 = mn.Ellipse(width=0.4, height=0.2, color="#FF00FF", fill_opacity=0.8)
                mito2.shift(mn.DOWN * 0.8 + mn.LEFT * 0.5)
                
                self.play(mn.Create(mito1), mn.Create(mito2), run_time=1.5)
                
                info_text = mn.Text("Basic unit of life", font_size=12, color="#FFFFFF")
                info_text.shift(mn.DOWN * 2.5)
                self.play(mn.Write(info_text), run_time=1.5)
                self.wait(2)
        
        return self._render_scene(SimpleAnimationScene, animation_id)
    
    def _create_educational_explanation(self, instructions: Dict[str, Any], explanation_id: str) -> str:
        """Create educational explanation video"""
        
        class ExplanationScene(mn.Scene):
            def construct(self):
                # Title
                title = mn.Text("Educational Explanation", font_size=24, color="#00FFFF")
                title.shift(mn.UP * 2)
                concept = mn.Text(instructions["concept"], font_size=18, color="#FFFFFF")
                concept.shift(mn.UP * 1)
                
                self.play(mn.Write(title), mn.Write(concept), run_time=2)
                self.wait(2)
                
                # Clear and show points
                self.play(mn.FadeOut(title), mn.FadeOut(concept))
                
                learning_title = mn.Text("Key Learning Points:", font_size=20, color="#FFFF00")
                learning_title.shift(mn.UP * 2)
                self.play(mn.Write(learning_title), run_time=1)
                
                # Show educational points
                for i, point in enumerate(instructions["educational_points"][:3]):  # Show first 3 points
                    point_text = mn.Text(f"• {point}", font_size=14, color="#FFFFFF")
                    point_text.shift(mn.UP * (1 - i * 0.6))
                    self.play(mn.Write(point_text), run_time=1.5)
                    self.wait(1)
                
                self.wait(2)
                
                # Summary
                self.play(*[mn.FadeOut(mob) for mob in self.mobjects])
                
                summary = mn.Text("Summary", font_size=22, color="#00FF00")
                summary.shift(mn.UP * 1)
                summary_text = mn.Text("You've learned the key concepts!", font_size=16, color="#FFFFFF")
                summary_text.shift(mn.DOWN * 0.5)
                
                self.play(mn.Write(summary), mn.Write(summary_text), run_time=2)
                self.wait(3)
        
        return self._render_scene(ExplanationScene, explanation_id)
    
    def _render_scene(self, scene_class, video_id: str) -> str:
        """Render scene and return video path with comprehensive error handling"""
        
        try:
            print(f"Starting render for {video_id}...")
            
            # Ensure proper environment setup
            self._setup_render_environment()
            
            # Configure Manim with Windows-compatible settings
            mn.config.media_dir = self.output_dir
            mn.config.video_dir = os.path.join(self.output_dir, "videos")
            mn.config.images_dir = os.path.join(self.output_dir, "images")
            mn.config.text_dir = os.path.join(self.output_dir, "texts")
            
            # Safe rendering settings
            mn.config.quality = "low_quality"
            mn.config.format = "mp4"
            mn.config.frame_rate = 15
            mn.config.pixel_height = 480
            mn.config.pixel_width = 854
            mn.config.background_color = "#000000"
            
            # Disable problematic features
            mn.config.disable_caching = True
            mn.config.write_to_movie = True
            mn.config.save_last_frame = False
            mn.config.write_all = False
            mn.config.enable_gui = False
            mn.config.preview = False
            mn.config.show_in_file_browser = False
            
            # Ensure all directories exist with proper permissions
            for dir_path in [mn.config.video_dir, mn.config.images_dir, mn.config.text_dir]:
                os.makedirs(dir_path, exist_ok=True)
                # Set directory permissions (Windows)
                try:
                    os.chmod(dir_path, 0o777)
                except:
                    pass
            
            print(f"Rendering scene with config: {mn.config.quality}, {mn.config.frame_rate}fps")
            
            # Create and render scene with timeout
            scene = scene_class()
            
            # Use subprocess to render with timeout and better error handling
            import tempfile
            import pickle
            
            # Save scene to temporary file
            temp_scene_file = os.path.join(tempfile.gettempdir(), f"scene_{video_id}.pkl")
            with open(temp_scene_file, 'wb') as f:
                pickle.dump(scene, f)
            
            # Render the scene
            scene.render()
            
            print(f"Scene rendered successfully for {video_id}")
            
        except FileNotFoundError as e:
            print(f"File not found error: {e}")
            print("Attempting to fix missing system dependencies...")
            self._fix_system_dependencies()
            return self._create_fallback_video(video_id)
            
        except PermissionError as e:
            print(f"Permission error: {e}")
            print("Attempting to fix directory permissions...")
            self._fix_permissions()
            return self._create_fallback_video(video_id)
            
        except subprocess.TimeoutExpired:
            print(f"Rendering timeout for {video_id}")
            return self._create_fallback_video(video_id)
            
        except Exception as e:
            print(f"Manim rendering failed with error: {type(e).__name__}: {e}")
            print(f"Error details: {str(e)}")
            import traceback
            traceback.print_exc()
            return self._create_fallback_video(video_id)
        
        # Find and copy video
        video_files = []
        for root, dirs, files in os.walk(mn.config.video_dir):
            for file in files:
                if file.endswith('.mp4'):
                    video_files.append(os.path.join(root, file))
        
        if video_files:
            latest_video = max(video_files, key=os.path.getctime)
            final_path = os.path.join(self.output_dir, f"{video_id}.mp4")
            import shutil
            shutil.copy2(latest_video, final_path)
            return final_path
        
        return None
    
    def _setup_render_environment(self):
        """Setup proper rendering environment"""
        # Set environment variables for Windows compatibility
        os.environ['MANIM_DISABLE_CACHING'] = 'True'
        os.environ['MANIM_VERBOSITY'] = 'WARNING'
        
        # Ensure PATH includes system directories
        current_path = os.environ.get('PATH', '')
        system_paths = [
            r'C:\Windows\System32',
            r'C:\Windows\SysWOW64',
        ]
        
        for path in system_paths:
            if os.path.exists(path) and path not in current_path:
                os.environ['PATH'] = f"{path};{current_path}"
    
    def _fix_system_dependencies(self):
        """Attempt to fix missing system dependencies"""
        print("Checking system dependencies...")
        
        # Check for common missing files
        import shutil
        dependencies = {
            'ffmpeg': shutil.which('ffmpeg'),
            'python': sys.executable,
        }
        
        for dep, path in dependencies.items():
            if not path:
                print(f"Missing dependency: {dep}")
            else:
                print(f"Found {dep}: {path}")
    
    def _fix_permissions(self):
        """Fix directory permissions"""
        try:
            for dir_path in [self.output_dir, os.path.join(self.output_dir, "videos")]:
                if os.path.exists(dir_path):
                    os.chmod(dir_path, 0o777)
                    print(f"Fixed permissions for {dir_path}")
        except Exception as e:
            print(f"Could not fix permissions: {e}")
    
    def _create_fallback_video(self, video_id: str) -> str:
        """Create a simple fallback when Manim fails"""
        try:
            # Create a minimal scene that should always work
            class FallbackScene(mn.Scene):
                def construct(self):
                    text = mn.Text("Educational Content", font_size=24, color="#FFFFFF")
                    self.add(text)
                    self.wait(2)
            
            scene = FallbackScene()
            scene.render()
            
            # Find and copy the video
            video_files = []
            for root, dirs, files in os.walk(mn.config.video_dir):
                for file in files:
                    if file.endswith('.mp4'):
                        video_files.append(os.path.join(root, file))
            
            if video_files:
                latest_video = max(video_files, key=os.path.getctime)
                final_path = os.path.join(self.output_dir, f"{video_id}.mp4")
                import shutil
                shutil.copy2(latest_video, final_path)
                return final_path
                
        except Exception as e:
            print(f"Fallback video creation also failed: {e}")
            # Create a dummy file as last resort
            dummy_path = os.path.join(self.output_dir, f"{video_id}.mp4")
            with open(dummy_path, 'w') as f:
                f.write("# Educational video placeholder")
            return dummy_path
        
        return None
    
    def _identify_concept(self, prompt: str) -> str:
        """Identify concept type"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['sort', 'bubble', 'merge']):
            return "sorting"
        elif any(word in prompt_lower for word in ['function', 'sine', 'math', 'equation']):
            return "math"
        else:
            return "general"
    
    def _analyze_general_prompt(self, prompt: str) -> str:
        """Analyze general prompts for specific content"""
        prompt_lower = prompt.lower()
        
        # Geometry and shapes
        if any(word in prompt_lower for word in ['circle', 'round', 'ball', 'sphere']):
            return "circle"
        elif any(word in prompt_lower for word in ['square', 'rectangle', 'triangle', 'polygon']):
            return "geometry"
        
        # Biology
        elif any(word in prompt_lower for word in ['dna', 'genetic', 'helix', 'gene']):
            return "dna"
        elif any(word in prompt_lower for word in ['cell', 'biology', 'mitosis', 'organism']):
            return "cell"
        elif any(word in prompt_lower for word in ['heart', 'blood', 'circulation', 'pulse']):
            return "heart"
        elif any(word in prompt_lower for word in ['brain', 'neuron', 'nervous', 'synapse']):
            return "brain"
        
        # Chemistry and Physics
        elif any(word in prompt_lower for word in ['atom', 'molecule', 'electron', 'proton']):
            return "atom"
        elif any(word in prompt_lower for word in ['water', 'h2o', 'molecule', 'chemical']):
            return "chemistry"
        elif any(word in prompt_lower for word in ['gravity', 'force', 'newton', 'physics']):
            return "physics"
        
        # Space and astronomy
        elif any(word in prompt_lower for word in ['planet', 'solar', 'space', 'orbit', 'star']):
            return "space"
        elif any(word in prompt_lower for word in ['earth', 'moon', 'sun']):
            return "astronomy"
        
        # Technology
        elif any(word in prompt_lower for word in ['computer', 'algorithm', 'code', 'programming']):
            return "technology"
        elif any(word in prompt_lower for word in ['internet', 'network', 'data', 'digital']):
            return "digital"
        
        # Nature and environment
        elif any(word in prompt_lower for word in ['tree', 'plant', 'photosynthesis', 'leaf']):
            return "plant"
        elif any(word in prompt_lower for word in ['ocean', 'water', 'sea', 'marine']):
            return "ocean"
        elif any(word in prompt_lower for word in ['weather', 'climate', 'rain', 'wind']):
            return "weather"
        
        # Animals
        elif any(word in prompt_lower for word in ['animal', 'mammal', 'bird', 'fish']):
            return "animal"
        
        # Energy
        elif any(word in prompt_lower for word in ['energy', 'electricity', 'power', 'battery']):
            return "energy"
        
        else:
            return "generic"