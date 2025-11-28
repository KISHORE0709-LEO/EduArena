from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from manim_config_fix import setup_manim_environment
import uuid
import os

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
            title = mn.Text(f"Animation: {description}", font_size=24)
            title.to_edge(mn.UP)
            
            if "bernoulli" in description.lower():
                # Bernoulli's Principle - Complete Animation
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                # Create airfoil
                airfoil = mn.Ellipse(width=4, height=1, color=mn.BLUE)
                airfoil.set_fill(mn.BLUE, opacity=0.3)
                self.play(mn.Create(airfoil), run_time=2)
                
                # Air flow streamlines
                flow_lines = mn.VGroup()
                for i in range(7):
                    if i < 3:  # Top - faster flow
                        line = mn.Arrow(start=mn.LEFT * 4, end=mn.RIGHT * 4, color=mn.RED, stroke_width=3)
                        line.shift(mn.UP * (i + 1) * 0.5)
                    elif i > 3:  # Bottom - slower flow
                        line = mn.Arrow(start=mn.LEFT * 4, end=mn.RIGHT * 4, color=mn.GREEN, stroke_width=5)
                        line.shift(mn.DOWN * (i - 3) * 0.5)
                    else:
                        line = mn.Arrow(start=mn.LEFT * 4, end=mn.RIGHT * 4, color="#00FFFF", stroke_width=4)
                    flow_lines.add(line)
                
                self.play(mn.Create(flow_lines), run_time=3)
                self.wait(2)
                
                # Velocity and pressure labels
                top_text = mn.Text("Higher Velocity\nLower Pressure", font_size=16, color=mn.RED)
                top_text.next_to(airfoil, mn.UP, buff=1)
                
                bottom_text = mn.Text("Lower Velocity\nHigher Pressure", font_size=16, color=mn.GREEN)
                bottom_text.next_to(airfoil, mn.DOWN, buff=1)
                
                self.play(mn.Write(top_text), mn.Write(bottom_text), run_time=3)
                self.wait(2)
                
                # Pressure arrows
                pressure_up = mn.VGroup()
                for i in range(5):
                    arrow = mn.Arrow(start=mn.DOWN * 0.8, end=mn.UP * 0.3, color=mn.GREEN, stroke_width=4)
                    arrow.shift(mn.LEFT * (i - 2) * 0.8)
                    pressure_up.add(arrow)
                
                pressure_down = mn.VGroup()
                for i in range(5):
                    arrow = mn.Arrow(start=mn.UP * 0.8, end=mn.DOWN * 0.2, color=mn.RED, stroke_width=2)
                    arrow.shift(mn.LEFT * (i - 2) * 0.8)
                    pressure_down.add(arrow)
                
                self.play(mn.Create(pressure_up), mn.Create(pressure_down), run_time=2)
                self.wait(1)
                
                # Net lift force
                lift_arrow = mn.Arrow(start=airfoil.get_center(), end=airfoil.get_center() + mn.UP * 2.5, 
                                    color="#FFFF00", stroke_width=8)
                lift_label = mn.Text("LIFT FORCE", font_size=20, color="#FFFF00")
                lift_label.next_to(lift_arrow, mn.RIGHT)
                
                self.play(mn.Create(lift_arrow), mn.Write(lift_label), run_time=2)
                self.wait(2)
                
                # Bernoulli's equation
                equation = mn.MathTex(r"P + \frac{1}{2}\rho v^2 = \text{constant}", font_size=24)
                equation.to_edge(mn.DOWN)
                self.play(mn.Write(equation), run_time=3)
                self.wait(3)
                
                # Applications
                apps = mn.Text("Applications: Aircraft Wings, Carburetors, Venturi Tubes", font_size=14, color="#FFA500")
                apps.next_to(equation, mn.UP, buff=0.3)
                self.play(mn.Write(apps), run_time=2)
                self.wait(4)
            
            elif "matrix" in description.lower() and "exponentiation" in description.lower():
                # 4x4 Matrix Exponentiation
                self.play(mn.Write(title), run_time=2)
                self.wait(1)
                
                # Create 4x4 matrix
                matrix_entries = [["a", "b", "c", "d"],
                                ["e", "f", "g", "h"],
                                ["i", "j", "k", "l"],
                                ["m", "n", "o", "p"]]
                
                matrix = mn.Matrix(matrix_entries)
                matrix.set_color("#00FFFF")
                self.play(mn.Create(matrix), run_time=3)
                self.wait(2)
                
                # Exponentiation concept
                exp_text = mn.Text("Matrix Exponentiation: A^n", font_size=20, color="#FFFF00")
                exp_text.next_to(matrix, mn.UP, buff=1)
                self.play(mn.Write(exp_text), run_time=2)
                self.wait(2)
                
                # Show A^2 = A × A
                times = mn.Text("×", font_size=30, color="#FFFFFF")
                matrix2 = matrix.copy()
                
                group = mn.VGroup(matrix, times, matrix2)
                group.arrange(mn.RIGHT, buff=0.5)
                
                self.play(mn.Transform(matrix, group[0]), run_time=2)
                self.play(mn.Write(times), mn.Create(matrix2), run_time=2)
                self.wait(2)
                
                # Result matrix
                equals = mn.Text("=", font_size=30, color="#FFFFFF")
                result = mn.Matrix([["r11", "r12", "r13", "r14"],
                                  ["r21", "r22", "r23", "r24"],
                                  ["r31", "r32", "r33", "r34"],
                                  ["r41", "r42", "r43", "r44"]])
                result.set_color("#00FF00")
                
                result_group = mn.VGroup(equals, result)
                result_group.arrange(mn.RIGHT, buff=0.3)
                result_group.next_to(group, mn.RIGHT, buff=0.5)
                
                self.play(mn.Write(equals), mn.Create(result), run_time=3)
                self.wait(2)
                
                # Applications
                apps_text = mn.Text("Applications:\n• Graph algorithms\n• Dynamic programming\n• Linear recurrences", 
                                  font_size=16, color="#00FFFF")
                apps_text.to_edge(mn.DOWN)
                self.play(mn.Write(apps_text), run_time=3)
                self.wait(4)
            
            elif "bubble sort" in description.lower():
                # Bubble sort with complete passes
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
                self.play(mn.Create(squares), mn.Write(labels), run_time=2)
                self.wait(1)
                
                # Complete bubble sort
                for pass_num in range(len(numbers)):
                    for i in range(len(numbers) - 1 - pass_num):
                        # Highlight comparison
                        self.play(
                            squares[i].animate.set_fill(mn.RED, opacity=0.7),
                            squares[i+1].animate.set_fill(mn.RED, opacity=0.7),
                            run_time=0.5
                        )
                        self.wait(0.5)
                        
                        # Swap if needed
                        if numbers[i] > numbers[i+1]:
                            self.play(
                                squares[i].animate.shift(mn.RIGHT * 1.2),
                                squares[i+1].animate.shift(mn.LEFT * 1.2),
                                labels[i].animate.shift(mn.RIGHT * 1.2),
                                labels[i+1].animate.shift(mn.LEFT * 1.2),
                                run_time=1
                            )
                            
                            # Update arrays
                            squares[i], squares[i+1] = squares[i+1], squares[i]
                            labels[i], labels[i+1] = labels[i+1], labels[i]
                            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                        
                        # Reset colors
                        self.play(
                            squares[i].animate.set_fill(mn.BLUE, opacity=0.7),
                            squares[i+1].animate.set_fill(mn.BLUE, opacity=0.7),
                            run_time=0.3
                        )
                    
                    # Mark sorted
                    self.play(squares[len(numbers) - 1 - pass_num].animate.set_fill(mn.GREEN, opacity=0.7), run_time=0.5)
                    self.wait(0.5)
                
                # Final message
                final = mn.Text("Sorting Complete!", font_size=24, color="#00FF00")
                final.next_to(squares, mn.DOWN, buff=1)
                self.play(mn.Write(final), run_time=2)
                self.wait(3)
            
            else:
                circle = mn.Circle(radius=1)
                circle.set_fill(mn.BLUE, opacity=0.7)
                
                text = mn.Text("Educational Animation", font_size=20)
                text.next_to(circle, mn.DOWN)
                
                self.play(mn.Write(title))
                self.play(mn.Create(circle), mn.Write(text))
                self.play(circle.animate.set_fill(mn.RED, opacity=0.7))
                self.wait(2)
    
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
            "instructions": {
                "concept": description,
                "description": f"Educational animation for: {description}",
                "scenes": [
                    {
                        "id": 1,
                        "title": "Introduction",
                        "duration": "2s",
                        "action": "Display title and setup"
                    },
                    {
                        "id": 2,
                        "title": "Main Animation",
                        "duration": "4s",
                        "action": "Core concept demonstration"
                    },
                    {
                        "id": 3,
                        "title": "Conclusion",
                        "duration": "2s",
                        "action": "Final state and summary"
                    }
                ],
                "educational_points": [
                    f"Understanding {description} concept",
                    "Visual representation of the process",
                    "Step-by-step breakdown",
                    "Real-world applications"
                ]
            }
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