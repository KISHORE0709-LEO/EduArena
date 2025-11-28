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
    
    try:
        if "bernoulli" in description.lower():
            class BernoulliScene(mn.Scene):
                def construct(self):
                    # Title with EduArena theme
                    title = mn.Text("Bernoulli's Principle", font_size=36, color=mn.BLUE).to_edge(mn.UP)
                    
                    # Create axes for flow visualization
                    axes = mn.Axes(
                        x_range=[-5, 5, 1],
                        y_range=[-3, 3, 1],
                        axis_config={"include_tip": True},
                        x_length=10,
                        y_length=6
                    )
                    
                    # Airfoil shape using parametric curve
                    airfoil = mn.ParametricFunction(
                        lambda t: axes.c2p(t, 0.3 * mn.np.sin(mn.np.pi * t) * mn.np.exp(-0.1 * t**2)),
                        t_range=[-4, 4],
                        color=mn.BLUE
                    )
                    airfoil.set_fill(mn.BLUE, opacity=0.3)
                    
                    # Flow streamlines with different velocities
                    flow_lines = mn.VGroup()
                    for i in range(7):
                        y_pos = (i - 3) * 0.8
                        if abs(y_pos) < 1:  # Near airfoil - faster flow
                            line = mn.Arrow(start=axes.c2p(-4, y_pos), end=axes.c2p(4, y_pos), color=mn.RED, stroke_width=3)
                        else:  # Away from airfoil - slower flow
                            line = mn.Arrow(start=axes.c2p(-4, y_pos), end=axes.c2p(4, y_pos), color=mn.GREEN, stroke_width=5)
                        flow_lines.add(line)
                    
                    # Pressure indicators
                    high_pressure = mn.VGroup()
                    low_pressure = mn.VGroup()
                    
                    for i in range(5):
                        x_pos = (i - 2) * 1.5
                        # High pressure below
                        hp_arrow = mn.Arrow(start=axes.c2p(x_pos, -2), end=axes.c2p(x_pos, -1), color=mn.GREEN, stroke_width=4)
                        high_pressure.add(hp_arrow)
                        # Low pressure above
                        lp_arrow = mn.Arrow(start=axes.c2p(x_pos, 2), end=axes.c2p(x_pos, 1), color=mn.RED, stroke_width=2)
                        low_pressure.add(lp_arrow)
                    
                    # Labels
                    velocity_label = mn.Text("Flow Velocity", font_size=20, color=mn.YELLOW).next_to(axes.x_axis, mn.DOWN)
                    pressure_label = mn.Text("Pressure Distribution", font_size=20, color=mn.YELLOW).next_to(axes.y_axis, mn.LEFT)
                    
                    # Bernoulli equation
                    equation = mn.MathTex(
                        r"P + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}",
                        font_size=28,
                        color=mn.CYAN
                    ).to_edge(mn.DOWN)
                    
                    # Net lift force
                    lift_arrow = mn.Arrow(
                        start=axes.c2p(0, 0),
                        end=axes.c2p(0, 2.5),
                        color=mn.YELLOW,
                        stroke_width=8
                    )
                    lift_label = mn.Text("LIFT FORCE", font_size=24, color=mn.YELLOW).next_to(lift_arrow, mn.RIGHT)
                    
                    # Animate everything
                    self.play(mn.Write(title))
                    self.play(mn.Create(axes), mn.Write(velocity_label), mn.Write(pressure_label))
                    self.play(mn.Create(airfoil))
                    self.play(mn.Create(flow_lines), run_time=3)
                    self.play(mn.Create(high_pressure), mn.Create(low_pressure), run_time=2)
                    self.play(mn.Create(lift_arrow), mn.Write(lift_label))
                    self.play(mn.Write(equation), run_time=3)
                    self.wait(3)
            
            scene = BernoulliScene()
            scene.render()
            
        elif "matrix" in description.lower():
            class MatrixScene(mn.Scene):
                def construct(self):
                    # Title with EduArena theme
                    title = mn.Text("4x4 Matrix Exponentiation", font_size=36, color=mn.BLUE).to_edge(mn.UP)
                    
                    # Create 4x4 matrix A with themed styling
                    matrix_a = mn.VGroup(
                        mn.Text("a  b  c  d", color=mn.CYAN),
                        mn.Text("e  f  g  h", color=mn.CYAN),
                        mn.Text("i  j  k  l", color=mn.CYAN),
                        mn.Text("m  n  o  p", color=mn.CYAN)
                    ).arrange(mn.DOWN)
                    matrix_a.add(mn.SurroundingRectangle(matrix_a, color=mn.BLUE, buff=0.3))
                    
                    # Exponentiation concept
                    exp_label = mn.Text("A^n =", font_size=24, color=mn.YELLOW)
                    
                    # Multiplication symbols
                    times1 = mn.Text("×", font_size=30, color=mn.WHITE)
                    times2 = mn.Text("×", font_size=30, color=mn.WHITE)
                    times3 = mn.Text("× ...", font_size=30, color=mn.WHITE)
                    
                    # Multiple matrix copies
                    matrix_b = matrix_a.copy()
                    matrix_c = matrix_a.copy()
                    
                    # Arrange multiplication
                    multiplication = mn.VGroup(
                        exp_label, matrix_a, times1, matrix_b, times2, matrix_c, times3
                    ).arrange(mn.RIGHT, buff=0.3)
                    
                    # Step-by-step calculation for A^2
                    calc_title = mn.Text("For A^2 = A × A:", font_size=20, color=mn.YELLOW)
                    
                    # Show element calculation
                    calc1 = mn.Text("Element (1,1) = a×a + b×e + c×i + d×m", font_size=16, color=mn.GREEN)
                    calc2 = mn.Text("Element (1,2) = a×b + b×f + c×j + d×n", font_size=16, color=mn.GREEN)
                    calc3 = mn.Text("... (16 total calculations)", font_size=16, color=mn.GREEN)
                    
                    calculations = mn.VGroup(calc_title, calc1, calc2, calc3).arrange(mn.DOWN, aligned_edge=mn.LEFT)
                    calculations.next_to(multiplication, mn.DOWN, buff=1)
                    
                    # Result matrix
                    result_matrix = mn.VGroup(
                        mn.Text("r₁₁ r₁₂ r₁₃ r₁₄", color=mn.GREEN),
                        mn.Text("r₂₁ r₂₂ r₂₃ r₂₄", color=mn.GREEN),
                        mn.Text("r₃₁ r₃₂ r₃₃ r₃₄", color=mn.GREEN),
                        mn.Text("r₄₁ r₄₂ r₄₃ r₄₄", color=mn.GREEN)
                    ).arrange(mn.DOWN)
                    result_matrix.add(mn.SurroundingRectangle(result_matrix, color=mn.GREEN, buff=0.3))
                    
                    equals = mn.Text("=", font_size=30, color=mn.WHITE)
                    result_group = mn.VGroup(equals, result_matrix).arrange(mn.RIGHT, buff=0.3)
                    result_group.next_to(calculations, mn.DOWN, buff=1)
                    
                    # Applications
                    apps_title = mn.Text("Applications:", font_size=20, color=mn.YELLOW)
                    app1 = mn.Text("• Graph path counting (A^n paths of length n)", font_size=16, color=mn.ORANGE)
                    app2 = mn.Text("• Linear recurrence relations", font_size=16, color=mn.ORANGE)
                    app3 = mn.Text("• Dynamic programming optimization", font_size=16, color=mn.ORANGE)
                    
                    applications = mn.VGroup(apps_title, app1, app2, app3).arrange(mn.DOWN, aligned_edge=mn.LEFT)
                    applications.to_edge(mn.DOWN)
                    
                    # Animate everything
                    self.play(mn.Write(title))
                    self.play(mn.Create(matrix_a))
                    self.play(mn.Write(exp_label))
                    self.play(mn.Write(times1), mn.Create(matrix_b))
                    self.play(mn.Write(times2), mn.Create(matrix_c), mn.Write(times3))
                    self.wait(2)
                    
                    self.play(mn.Write(calc_title))
                    self.play(mn.Write(calc1))
                    self.play(mn.Write(calc2))
                    self.play(mn.Write(calc3))
                    self.wait(2)
                    
                    self.play(mn.Write(equals), mn.Create(result_matrix))
                    self.wait(2)
                    
                    self.play(mn.Write(apps_title))
                    self.play(mn.Write(app1))
                    self.play(mn.Write(app2))
                    self.play(mn.Write(app3))
                    self.wait(3)
            
            scene = MatrixScene()
            scene.render()
        
        else:
            return jsonify({"error": "Only Bernoulli and Matrix supported"})
        
        session_id = str(uuid.uuid4())[:8]
        return jsonify({
            "success": True,
            "session_id": session_id,
            "video_url": f"/video/{session_id}",
            "message": "Animation generated successfully",
            "instructions": {
                "concept": "Bernoulli's Principle" if "bernoulli" in description.lower() else "4x4 Matrix Exponentiation",
                "description": "Complete educational animation with detailed explanation",
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": "3s", "action": "Display title"},
                    {"id": 2, "title": "Main Content", "duration": "15s", "action": "Core demonstration"},
                    {"id": 3, "title": "Conclusion", "duration": "4s", "action": "Summary"}
                ],
                "educational_points": [
                    "Visual demonstration of key concepts",
                    "Mathematical foundations and equations", 
                    "Real-world applications and uses",
                    "Step-by-step educational breakdown"
                ]
            }
        })
        
    except Exception as e:
        return jsonify({"error": f"Animation generation failed: {str(e)}"})

@app.route('/video/<session_id>')
def serve_video(session_id):
    media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media", "videos")
    
    for root, dirs, files in os.walk(media_dir):
        for file in files:
            if file.endswith('.mp4'):
                video_path = os.path.join(root, file)
                return send_file(video_path, mimetype='video/mp4')
    
    return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)