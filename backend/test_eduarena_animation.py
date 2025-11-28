import os
import sys
from manim_config_fix import setup_manim_environment

def test_eduarena_animation():
    """Test EduArena animation generation"""
    
    # Setup Manim environment
    if not setup_manim_environment():
        print("Failed to setup Manim environment")
        return False
    
    try:
        import manim as mn
        
        class BubbleSortScene(mn.Scene):
            def construct(self):
                # Create array of numbers
                numbers = [64, 34, 25, 12, 22, 11, 90]
                
                # Create visual representation
                squares = mn.VGroup()
                labels = mn.VGroup()
                
                for i, num in enumerate(numbers):
                    square = mn.Square(side_length=0.8)
                    square.set_fill(mn.BLUE, opacity=0.7)
                    square.shift(mn.RIGHT * (i - 3) * 1.2)
                    
                    label = mn.Text(str(num), font_size=24)
                    label.move_to(square.get_center())
                    
                    squares.add(square)
                    labels.add(label)
                
                # Add title
                title = mn.Text("Bubble Sort Animation", font_size=36)
                title.to_edge(mn.UP)
                
                # Show initial state
                self.play(mn.Write(title))
                self.play(mn.Create(squares), mn.Write(labels))
                self.wait(1)
                
                # Simple bubble sort animation (first pass only for demo)
                for i in range(len(numbers) - 1):
                    # Highlight comparison
                    self.play(
                        squares[i].animate.set_fill(mn.RED, opacity=0.7),
                        squares[i+1].animate.set_fill(mn.RED, opacity=0.7)
                    )
                    self.wait(0.5)
                    
                    # Swap if needed
                    if numbers[i] > numbers[i+1]:
                        # Animate swap
                        self.play(
                            squares[i].animate.shift(mn.RIGHT * 1.2),
                            squares[i+1].animate.shift(mn.LEFT * 1.2),
                            labels[i].animate.shift(mn.RIGHT * 1.2),
                            labels[i+1].animate.shift(mn.LEFT * 1.2)
                        )
                        
                        # Update arrays
                        squares[i], squares[i+1] = squares[i+1], squares[i]
                        labels[i], labels[i+1] = labels[i+1], labels[i]
                        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    
                    # Reset colors
                    self.play(
                        squares[i].animate.set_fill(mn.BLUE, opacity=0.7),
                        squares[i+1].animate.set_fill(mn.BLUE, opacity=0.7)
                    )
                
                self.wait(2)
        
        # Render the scene
        scene = BubbleSortScene()
        scene.render()
        
        print("EduArena animation test successful!")
        print(f"Video saved in: {mn.config.media_dir}")
        return True
        
    except Exception as e:
        print(f"EduArena animation test failed: {e}")
        return False

if __name__ == "__main__":
    test_eduarena_animation()