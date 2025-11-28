from manim_config_fix import setup_manim_environment
import json
import uuid

def test_all_eduarena_components():
    """Test all three EduArena components"""
    
    if not setup_manim_environment():
        return False
    
    import manim as mn
    
    # 1. STRUCTURED ANIMATION INSTRUCTIONS
    animation_instructions = {
        "concept": "bubble_sort",
        "steps": [
            {"action": "create_array", "data": [64, 34, 25, 12, 22]},
            {"action": "highlight_comparison", "indices": [0, 1]},
            {"action": "swap_elements", "indices": [0, 1]},
            {"action": "move_to_next", "current": 1}
        ],
        "metadata": {
            "duration": 10,
            "difficulty": "beginner",
            "subject": "algorithms"
        }
    }
    
    # 2. RENDERED VISUAL ANIMATION
    class EducationalScene(mn.Scene):
        def construct(self):
            title = mn.Text("Bubble Sort Algorithm", font_size=32)
            title.to_edge(mn.UP)
            
            # Create array visualization
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
            
            # Demonstrate one swap
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
    
    # 3. EDUCATIONAL EXPLANATION VIDEO
    class ExplanationScene(mn.Scene):
        def construct(self):
            title = mn.Text("How Bubble Sort Works", font_size=36)
            title.to_edge(mn.UP)
            
            explanation = mn.VGroup(
                mn.Text("1. Compare adjacent elements", font_size=24),
                mn.Text("2. Swap if left > right", font_size=24),
                mn.Text("3. Repeat for all pairs", font_size=24),
                mn.Text("4. Continue until sorted", font_size=24)
            ).arrange(mn.DOWN, aligned_edge=mn.LEFT, buff=0.5)
            explanation.move_to(mn.ORIGIN)
            
            self.play(mn.Write(title))
            for step in explanation:
                self.play(mn.Write(step))
                self.wait(1)
            self.wait(2)
    
    try:
        # Generate unique ID for this session
        session_id = str(uuid.uuid4())[:8]
        
        # Render animation
        scene1 = EducationalScene()
        scene1.render()
        animation_file = f"{session_id}_animation.mp4"
        
        # Render explanation
        scene2 = ExplanationScene()
        scene2.render()
        explanation_file = f"{session_id}_explanation.mp4"
        
        print("SUCCESS: All three components working!")
        print(f"1. Animation Instructions: {json.dumps(animation_instructions, indent=2)}")
        print(f"2. Visual Animation: Generated successfully")
        print(f"3. Explanation Video: Generated successfully")
        print(f"Files saved in: {mn.config.media_dir}")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_all_eduarena_components()