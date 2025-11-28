#!/usr/bin/env python3
"""
Test script to verify Manim is working properly with the configuration
"""

import os
import sys
from manim_config_fix import setup_manim_environment

def test_basic_animation():
    """Test basic Manim animation generation"""
    
    # Setup environment first
    if not setup_manim_environment():
        print("Failed to setup Manim environment")
        return False
    
    try:
        import manim as mn
        
        class TestScene(mn.Scene):
            def construct(self):
                # Create simple text
                text = mn.Text("EduArena Test", font_size=48)
                self.add(text)
                
                # Create a circle
                circle = mn.Circle(radius=1, color=mn.BLUE)
                circle.next_to(text, mn.DOWN, buff=0.5)
                
                # Animate
                self.play(mn.Write(text))
                self.play(mn.Create(circle))
                self.play(circle.animate.set_color(mn.RED))
                self.wait(1)
        
        # Render the scene
        scene = TestScene()
        scene.render()
        
        # Check if video was created
        backend_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(backend_dir, "media", "videos", "480p15", "TestScene.mp4")
        
        if os.path.exists(video_path):
            print(f"SUCCESS: Animation created at {video_path}")
            print(f"File size: {os.path.getsize(video_path)} bytes")
            return True
        else:
            print("FAILED: No video file created")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Manim animation generation...")
    success = test_basic_animation()
    
    if success:
        print("\n✅ Manim is working correctly!")
        print("Your EduArena backend should be able to generate animations.")
    else:
        print("\n❌ Manim test failed!")
        print("Check the error messages above for troubleshooting.")