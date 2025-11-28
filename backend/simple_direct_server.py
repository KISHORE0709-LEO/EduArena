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
                    title = mn.Text("Bernoulli's Principle", font_size=32)
                    title.to_edge(mn.UP)
                    self.play(mn.Write(title), run_time=2)
                    self.wait(1)
                    
                    airfoil = mn.Ellipse(width=4, height=1)
                    airfoil.set_fill(mn.BLUE, opacity=0.3)
                    self.play(mn.Create(airfoil), run_time=2)
                    
                    flow_lines = mn.VGroup()
                    for i in range(5):
                        line = mn.Arrow(start=mn.LEFT * 4, end=mn.RIGHT * 4)
                        line.shift(mn.UP * (i - 2) * 0.8)
                        flow_lines.add(line)
                    
                    self.play(mn.Create(flow_lines), run_time=3)
                    self.wait(2)
                    
                    top_text = mn.Text("Higher Velocity\\nLower Pressure", font_size=16)
                    top_text.next_to(airfoil, mn.UP, buff=1)
                    
                    bottom_text = mn.Text("Lower Velocity\\nHigher Pressure", font_size=16)
                    bottom_text.next_to(airfoil, mn.DOWN, buff=1)
                    
                    self.play(mn.Write(top_text), mn.Write(bottom_text), run_time=3)
                    self.wait(2)
                    
                    lift_arrow = mn.Arrow(start=airfoil.get_center(), end=airfoil.get_center() + mn.UP * 2)
                    lift_label = mn.Text("LIFT", font_size=20)
                    lift_label.next_to(lift_arrow, mn.RIGHT)
                    
                    self.play(mn.Create(lift_arrow), mn.Write(lift_label), run_time=2)
                    self.wait(3)
                    
                    equation = mn.MathTex(r"P + \frac{1}{2}\rho v^2 = \text{constant}", font_size=24)
                    equation.to_edge(mn.DOWN)
                    self.play(mn.Write(equation), run_time=3)
                    self.wait(4)
            
            scene = BernoulliScene()
            
        elif "matrix" in description.lower():
            class MatrixScene(mn.Scene):
                def construct(self):
                    title = mn.Text("4x4 Matrix Exponentiation", font_size=28)
                    title.to_edge(mn.UP)
                    self.play(mn.Write(title), run_time=2)
                    self.wait(1)
                    
                    matrix_entries = [["a", "b", "c", "d"],
                                    ["e", "f", "g", "h"],
                                    ["i", "j", "k", "l"],
                                    ["m", "n", "o", "p"]]
                    
                    matrix = mn.Matrix(matrix_entries)
                    self.play(mn.Create(matrix), run_time=3)
                    self.wait(2)
                    
                    exp_text = mn.Text("A^n = A × A × ... × A", font_size=20)
                    exp_text.next_to(matrix, mn.UP, buff=1)
                    self.play(mn.Write(exp_text), run_time=2)
                    self.wait(2)
                    
                    times = mn.Text("×", font_size=30)
                    matrix2 = matrix.copy()
                    
                    group = mn.VGroup(matrix, times, matrix2)
                    group.arrange(mn.RIGHT, buff=0.5)
                    
                    self.play(mn.Transform(matrix, group[0]), run_time=2)
                    self.play(mn.Write(times), mn.Create(matrix2), run_time=2)
                    self.wait(2)
                    
                    equals = mn.Text("=", font_size=30)
                    result = mn.Matrix([["r11", "r12", "r13", "r14"],
                                      ["r21", "r22", "r23", "r24"],
                                      ["r31", "r32", "r33", "r34"],
                                      ["r41", "r42", "r43", "r44"]])
                    
                    result_group = mn.VGroup(equals, result)
                    result_group.arrange(mn.RIGHT, buff=0.3)
                    result_group.next_to(group, mn.RIGHT, buff=0.5)
                    
                    self.play(mn.Write(equals), mn.Create(result), run_time=3)
                    self.wait(2)
                    
                    apps = mn.Text("Applications: Graph algorithms, Dynamic programming", font_size=16)
                    apps.to_edge(mn.DOWN)
                    self.play(mn.Write(apps), run_time=3)
                    self.wait(4)
            
            scene = MatrixScene()
        
        else:
            return jsonify({"error": "Only Bernoulli and Matrix supported"})
        
        scene.render()
        
        session_id = str(uuid.uuid4())[:8]
        return jsonify({
            "success": True,
            "session_id": session_id,
            "video_url": f"/video/{session_id}",
            "message": "Animation generated successfully",
            "instructions": {
                "concept": "Bernoulli's Principle" if "bernoulli" in description.lower() else "4x4 Matrix Exponentiation",
                "description": "Complete educational animation",
                "scenes": [
                    {"id": 1, "title": "Introduction", "duration": "3s", "action": "Display title"},
                    {"id": 2, "title": "Main Content", "duration": "15s", "action": "Core demonstration"},
                    {"id": 3, "title": "Conclusion", "duration": "4s", "action": "Summary"}
                ],
                "educational_points": [
                    "Visual demonstration",
                    "Mathematical foundations", 
                    "Real-world applications"
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
                if os.path.exists(video_path):
                    return send_file(video_path, mimetype='video/mp4')
    
    return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)