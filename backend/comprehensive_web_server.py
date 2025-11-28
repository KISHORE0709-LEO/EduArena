from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from manim_config_fix import setup_manim_environment
import uuid
import os

def get_educational_breakdown(description):
    """Generate detailed educational breakdown based on description"""
    
    if "bubble sort" in description.lower():
        return {
            "concept": "Bubble Sort Algorithm",
            "description": "A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.",
            "scenes": [
                {"id": 1, "title": "Introduction", "duration": "4s", "action": "Display title and initial array"},
                {"id": 2, "title": "First Pass", "duration": "8s", "action": "Compare and swap adjacent elements"},
                {"id": 3, "title": "Subsequent Passes", "duration": "12s", "action": "Continue sorting with multiple passes"},
                {"id": 4, "title": "Completion", "duration": "4s", "action": "Show final sorted array"}
            ],
            "educational_points": [
                "Time complexity: O(n²) in worst case",
                "Space complexity: O(1) - in-place sorting",
                "Stable sorting algorithm",
                "Simple but inefficient for large datasets",
                "Good for educational purposes"
            ]
        }
    
    elif "bernoulli" in description.lower():
        return {
            "concept": "Bernoulli's Principle",
            "description": "A principle in fluid dynamics that states an increase in the speed of a fluid occurs simultaneously with a decrease in pressure.",
            "scenes": [
                {"id": 1, "title": "Introduction", "duration": "3s", "action": "Display title and concept overview"},
                {"id": 2, "title": "Airfoil Setup", "duration": "4s", "action": "Create airfoil shape and air flow"},
                {"id": 3, "title": "Velocity Differences", "duration": "6s", "action": "Show different air speeds above and below"},
                {"id": 4, "title": "Pressure & Lift", "duration": "5s", "action": "Demonstrate pressure differences and lift force"},
                {"id": 5, "title": "Mathematical Form", "duration": "4s", "action": "Display Bernoulli's equation"}
            ],
            "educational_points": [
                "Fundamental principle of fluid dynamics",
                "Explains how airplanes generate lift",
                "Conservation of energy in fluid flow",
                "Applications in aviation and engineering",
                "Relationship between velocity and pressure"
            ]
        }
    
    elif "matrix" in description.lower() and "exponentiation" in description.lower():
        return {
            "concept": "4x4 Matrix Exponentiation",
            "description": "The process of multiplying a matrix by itself multiple times, with applications in graph algorithms and dynamic programming.",
            "scenes": [
                {"id": 1, "title": "Matrix Introduction", "duration": "3s", "action": "Display 4x4 matrix structure"},
                {"id": 2, "title": "Exponentiation Concept", "duration": "4s", "action": "Explain A^n notation"},
                {"id": 3, "title": "Matrix Multiplication", "duration": "6s", "action": "Show A × A calculation"},
                {"id": 4, "title": "Result Matrix", "duration": "4s", "action": "Display resulting matrix"},
                {"id": 5, "title": "Applications", "duration": "4s", "action": "Show real-world uses"}
            ],
            "educational_points": [
                "Used in graph path counting algorithms",
                "Essential for solving linear recurrences",
                "Time complexity: O(n³) for naive approach",
                "Can be optimized using fast exponentiation",
                "Applications in computer graphics and AI"
            ]
        }
    
    else:
        return {
            "concept": description.title(),
            "description": f"Educational visualization and explanation of {description}",
            "scenes": [
                {"id": 1, "title": "Introduction", "duration": "3s", "action": "Display concept title"},
                {"id": 2, "title": "Visual Setup", "duration": "4s", "action": "Create visual elements"},
                {"id": 3, "title": "Core Animation", "duration": "8s", "action": "Demonstrate key concepts"},
                {"id": 4, "title": "Summary", "duration": "3s", "action": "Conclude with key takeaways"}
            ],
            "educational_points": [
                f"Understanding {description} fundamentals",
                "Visual representation of concepts",
                "Step-by-step explanation",
                "Practical applications",
                "Key learning objectives"
            ]
        }

app = Flask(__name__)
CORS(app)

@app.route('/generate-animation', methods=['POST'])
def generate_animation():
    data = request.json
    description = data.get('description', '')
    
    if not setup_manim_environment():
        return jsonify({"error": "Failed to setup environment"})
    
    import manim as mn
    
    class WebScene(mn.Scene):
        def construct(self):
            title = mn.Text(f"{description}", font_size=28, color=mn.CYAN)
            title.to_edge(mn.UP)
            
            if "bubble sort" in description.lower():
                # Complete bubble sort animation
                numbers = [64, 34, 25, 12, 22]
                squares = mn.VGroup()
                labels = mn.VGroup()
                
                for i, num in enumerate(numbers):
                    square = mn.Square(side_length=0.8)
                    square.set_fill(mn.BLUE, opacity=0.7)
                    square.shift(mn.RIGHT * (i - 2) * 1.2)
                    
                    label = mn.Text(str(num), font_size=20)
                    label.move_to(square.get_center())
                    
                    squares.add(square)
                    labels.add(label)
                
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                # Introduction
                intro = mn.Text("Bubble Sort Algorithm", font_size=24, color=mn.YELLOW)
                intro.next_to(title, mn.DOWN, buff=0.5)
                self.play(mn.Write(intro), run_time=2)
                self.wait(1)
                
                self.play(mn.Create(squares), mn.Write(labels), run_time=3)
                self.wait(2)
                
                # Complete sorting process
                for pass_num in range(len(numbers)):
                    for i in range(len(numbers) - 1 - pass_num):
                        # Highlight comparison
                        self.play(
                            squares[i].animate.set_fill(mn.RED, opacity=0.7),
                            squares[i+1].animate.set_fill(mn.RED, opacity=0.7),
                            run_time=1
                        )
                        self.wait(1)
                        
                        # Swap if needed
                        if numbers[i] > numbers[i+1]:
                            self.play(
                                squares[i].animate.shift(mn.RIGHT * 1.2),
                                squares[i+1].animate.shift(mn.LEFT * 1.2),
                                labels[i].animate.shift(mn.RIGHT * 1.2),
                                labels[i+1].animate.shift(mn.LEFT * 1.2),
                                run_time=2
                            )
                            
                            # Update arrays
                            squares[i], squares[i+1] = squares[i+1], squares[i]
                            labels[i], labels[i+1] = labels[i+1], labels[i]
                            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                        
                        # Reset colors
                        self.play(
                            squares[i].animate.set_fill(mn.BLUE, opacity=0.7),
                            squares[i+1].animate.set_fill(mn.BLUE, opacity=0.7),
                            run_time=0.5
                        )
                    
                    # Mark sorted element
                    self.play(squares[len(numbers) - 1 - pass_num].animate.set_fill(mn.GREEN, opacity=0.7), run_time=1)
                    self.wait(1)
                
                # Final message
                final = mn.Text("Sorting Complete!", font_size=24, color=mn.GREEN)
                final.next_to(squares, mn.DOWN, buff=1)
                self.play(mn.Write(final), run_time=2)
                self.wait(3)
            
            elif "bernoulli" in description.lower():
                # Bernoulli's Principle Animation
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                # Create airfoil shape
                airfoil = mn.Ellipse(width=4, height=1, color=mn.BLUE)
                airfoil.set_fill(mn.BLUE, opacity=0.3)
                self.play(mn.Create(airfoil), run_time=2)
                
                # Air flow lines
                flow_lines = mn.VGroup()
                for i in range(5):
                    line = mn.Arrow(start=mn.LEFT * 4, end=mn.RIGHT * 4, color=mn.CYAN)
                    line.shift(mn.UP * (i - 2) * 0.8)
                    flow_lines.add(line)
                
                self.play(mn.Create(flow_lines), run_time=3)
                self.wait(2)
                
                # Show velocity differences
                top_text = mn.Text("Higher Velocity\nLower Pressure", font_size=16, color=mn.RED)
                top_text.next_to(airfoil, mn.UP, buff=1)
                
                bottom_text = mn.Text("Lower Velocity\nHigher Pressure", font_size=16, color=mn.GREEN)
                bottom_text.next_to(airfoil, mn.DOWN, buff=1)
                
                self.play(mn.Write(top_text), mn.Write(bottom_text), run_time=3)
                self.wait(2)
                
                # Show lift force
                lift_arrow = mn.Arrow(start=airfoil.get_center(), end=airfoil.get_center() + mn.UP * 2, 
                                    color=mn.YELLOW, stroke_width=8)
                lift_label = mn.Text("LIFT", font_size=20, color=mn.YELLOW)
                lift_label.next_to(lift_arrow, mn.RIGHT)
                
                self.play(mn.Create(lift_arrow), mn.Write(lift_label), run_time=2)
                self.wait(3)
                
                # Equation
                equation = mn.MathTex(r"P + \frac{1}{2}\rho v^2 = \text{constant}", font_size=24)
                equation.to_edge(mn.DOWN)
                self.play(mn.Write(equation), run_time=3)
                self.wait(4)
            
            elif "matrix" in description.lower() and "exponentiation" in description.lower():
                # Matrix Exponentiation Animation
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                # Create 4x4 matrix
                matrix_entries = [["a", "b", "c", "d"],
                                ["e", "f", "g", "h"],
                                ["i", "j", "k", "l"],
                                ["m", "n", "o", "p"]]
                
                matrix = mn.Matrix(matrix_entries, bracket_h_buff=0.1, bracket_v_buff=0.1)
                matrix.set_color(mn.CYAN)
                
                self.play(mn.Create(matrix), run_time=3)
                self.wait(2)
                
                # Show exponentiation concept
                exp_text = mn.Text("Matrix Exponentiation: A^n", font_size=20, color=mn.YELLOW)
                exp_text.next_to(matrix, mn.UP, buff=1)
                self.play(mn.Write(exp_text), run_time=2)
                self.wait(2)
                
                # Show A^2 = A × A
                times_symbol = mn.Text("×", font_size=30, color=mn.WHITE)
                matrix2 = matrix.copy()
                
                group = mn.VGroup(matrix, times_symbol, matrix2)
                group.arrange(mn.RIGHT, buff=0.5)
                
                self.play(mn.Transform(matrix, group[0]), run_time=2)
                self.play(mn.Write(times_symbol), mn.Create(matrix2), run_time=2)
                self.wait(2)
                
                # Show result matrix
                equals = mn.Text("=", font_size=30, color=mn.WHITE)
                result_matrix = mn.Matrix([["r₁₁", "r₁₂", "r₁₃", "r₁₄"],
                                         ["r₂₁", "r₂₂", "r₂₃", "r₂₄"],
                                         ["r₃₁", "r₃₂", "r₃₃", "r₃₄"],
                                         ["r₄₁", "r₄₂", "r₄₃", "r₄₄"]])
                result_matrix.set_color(mn.GREEN)
                
                result_group = mn.VGroup(equals, result_matrix)
                result_group.arrange(mn.RIGHT, buff=0.3)
                result_group.next_to(group, mn.RIGHT, buff=0.5)
                
                self.play(mn.Write(equals), mn.Create(result_matrix), run_time=3)
                self.wait(2)
                
                # Show applications
                apps_text = mn.Text("Applications:\\n• Graph algorithms\\n• Dynamic programming\\n• Linear recurrences", 
                                  font_size=16, color=mn.CYAN)
                apps_text.to_edge(mn.DOWN)
                self.play(mn.Write(apps_text), run_time=3)
                self.wait(4)
            
            else:
                # Generic educational animation
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                circle = mn.Circle(radius=1.5, color=mn.CYAN)
                circle.set_fill(mn.BLUE, opacity=0.3)
                
                text = mn.Text("Educational Concept", font_size=24, color=mn.WHITE)
                text.next_to(circle, mn.DOWN, buff=1)
                
                self.play(mn.Create(circle), run_time=2)
                self.play(mn.Write(text), run_time=2)
                
                # Animate the circle
                self.play(circle.animate.set_fill(mn.RED, opacity=0.5), run_time=2)
                self.play(circle.animate.scale(1.2), run_time=2)
                self.play(circle.animate.scale(0.8), run_time=2)
                self.play(circle.animate.set_fill(mn.GREEN, opacity=0.7), run_time=2)
                
                final_text = mn.Text("Concept Explained!", font_size=20, color=mn.GREEN)
                final_text.next_to(text, mn.DOWN, buff=0.5)
                self.play(mn.Write(final_text), run_time=2)
                self.wait(3)
    
    try:
        session_id = str(uuid.uuid4())[:8]
        scene = WebScene()
        scene.render()
        
        video_path = "media/videos/480p15/WebScene.mp4"
        
        return jsonify({
            "success": True,
            "session_id": session_id,
            "video_url": f"/video/{session_id}",
            "message": "Animation generated successfully",
            "instructions": get_educational_breakdown(description)
        })
    
    except Exception as e:
        return jsonify({"error": f"Animation generation failed: {str(e)}"})

@app.route('/video/<session_id>')
def serve_video(session_id):
    video_path = os.path.join("media", "videos", "480p15", "WebScene.mp4")
    if os.path.exists(video_path):
        return send_file(video_path, mimetype='video/mp4')
    return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)