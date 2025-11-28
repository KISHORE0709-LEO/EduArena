from manim_config_fix import setup_manim_environment
import uuid

def generate_animation(description):
    """Generate animation from text description"""
    
    if not setup_manim_environment():
        return {"error": "Failed to setup environment"}
    
    import manim as mn
    
    class DynamicScene(mn.Scene):
        def construct(self):
            title = mn.Text(f"Animation: {description}", font_size=24)
            title.to_edge(mn.UP)
            
            if "bubble sort" in description.lower():
                # Bubble sort animation
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
                
                self.play(mn.Write(title))
                self.play(mn.Create(squares), mn.Write(labels))
                self.wait(1)
                
                # Simple swap animation
                self.play(
                    squares[0].animate.set_fill(mn.RED, opacity=0.7),
                    squares[1].animate.set_fill(mn.RED, opacity=0.7)
                )
                self.wait(0.5)
                
                if numbers[0] > numbers[1]:
                    self.play(
                        squares[0].animate.shift(mn.RIGHT * 1.2),
                        squares[1].animate.shift(mn.LEFT * 1.2),
                        labels[0].animate.shift(mn.RIGHT * 1.2),
                        labels[1].animate.shift(mn.LEFT * 1.2)
                    )
                
                self.wait(2)
            
            else:
                # Generic animation
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
        scene = DynamicScene()
        scene.render()
        
        return {
            "success": True,
            "session_id": session_id,
            "video_path": f"media/videos/480p15/DynamicScene.mp4",
            "message": "Animation generated successfully"
        }
    
    except Exception as e:
        return {"error": f"Animation generation failed: {str(e)}"}

if __name__ == "__main__":
    print("EduArena Animation Generator")
    print("=" * 40)
    
    while True:
        description = input("\nEnter animation description (or 'quit' to exit): ")
        
        if description.lower() == 'quit':
            break
        
        print("Generating animation...")
        result = generate_animation(description)
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Success: {result['message']}")
            print(f"Video saved at: {result['video_path']}")