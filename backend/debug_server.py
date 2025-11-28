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
    
    print(f"DEBUG: Received description: '{description}'")
    print(f"DEBUG: Description lower: '{description.lower()}'")
    print(f"DEBUG: 'bernoulli' in description.lower(): {'bernoulli' in description.lower()}")
    
    if not setup_manim_environment():
        return jsonify({"error": "Failed to setup environment"})
    
    import manim as mn
    
    class WebScene(mn.Scene):
        def construct(self):
            title = mn.Text(f"{description}", font_size=28, color=mn.CYAN)
            title.to_edge(mn.UP)
            
            print(f"DEBUG: Inside construct, checking conditions...")
            print(f"DEBUG: 'bernoulli' in description.lower(): {'bernoulli' in description.lower()}")
            
            if "bernoulli" in description.lower():
                print("DEBUG: Executing Bernoulli animation")
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
            
            else:
                print("DEBUG: Executing generic animation")
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
            "instructions": {
                "concept": "Bernoulli's Principle",
                "description": "Test animation",
                "scenes": [{"id": 1, "title": "Test", "duration": "10s", "action": "Test"}],
                "educational_points": ["Test point"]
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