import os
import sys
import subprocess
import shutil
from pathlib import Path

def setup_manim_environment():
    """Final setup for Manim environment with proper ffmpeg configuration"""
    
    # Get absolute paths
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
    
    # Verify ffmpeg exists
    if not os.path.exists(ffmpeg_path):
        print(f"FFmpeg not found at: {ffmpeg_path}")
        return False
    
    # Set environment variables for Manim
    os.environ['FFMPEG_BINARY'] = ffmpeg_path
    os.environ['MANIM_DISABLE_CACHING'] = 'True'
    os.environ['MANIM_VERBOSITY'] = 'WARNING'
    
    # Add ffmpeg directory to PATH
    ffmpeg_dir = os.path.dirname(ffmpeg_path)
    current_path = os.environ.get('PATH', '')
    if ffmpeg_dir not in current_path:
        os.environ['PATH'] = f"{ffmpeg_dir};{current_path}"
    
    # Set up temporary directories
    temp_dir = os.path.join(backend_dir, 'temp_manim')
    os.makedirs(temp_dir, exist_ok=True)
    os.environ['TEMP'] = temp_dir
    os.environ['TMP'] = temp_dir
    
    try:
        import manim as mn
        
        # Configure Manim with absolute paths
        mn.config.media_dir = os.path.join(backend_dir, "media")
        mn.config.log_dir = os.path.join(temp_dir, "logs")
        mn.config.tex_dir = os.path.join(temp_dir, "tex")
        mn.config.partial_movie_dir = os.path.join(temp_dir, "partial")
        
        # Ensure directories exist
        for dir_path in [mn.config.media_dir, mn.config.log_dir, mn.config.tex_dir, mn.config.partial_movie_dir]:
            os.makedirs(dir_path, exist_ok=True)
        
        # Set rendering configuration
        mn.config.quality = "low_quality"
        mn.config.format = "mp4"
        mn.config.frame_rate = 15
        mn.config.pixel_height = 480
        mn.config.pixel_width = 854
        mn.config.background_color = "#000000"
        mn.config.disable_caching = True
        mn.config.write_to_movie = True
        mn.config.save_last_frame = False
        mn.config.write_all = False
        mn.config.enable_gui = False
        mn.config.preview = False
        mn.config.show_in_file_browser = False
        mn.config.use_opengl_renderer = False
        
        # Set ffmpeg executable path directly in config
        mn.config.ffmpeg_executable = ffmpeg_path
        
        print("Manim environment configured successfully!")
        print(f"FFmpeg path: {ffmpeg_path}")
        print(f"Media directory: {mn.config.media_dir}")
        
        return True
        
    except ImportError:
        print("Manim not installed. Install with: pip install manim")
        return False
    except Exception as e:
        print(f"Error configuring Manim: {e}")
        return False

def test_manim_render():
    """Test if Manim can render a simple animation"""
    try:
        import manim as mn
        
        class TestScene(mn.Scene):
            def construct(self):
                circle = mn.Circle()
                self.add(circle)
                self.wait(1)
        
        # Try to render the test scene
        scene = TestScene()
        scene.render()
        
        print("Manim test render successful!")
        return True
        
    except Exception as e:
        print(f"Manim test render failed: {e}")
        return False

if __name__ == "__main__":
    print("Setting up Manim environment...")
    
    if setup_manim_environment():
        print("\nTesting Manim render...")
        test_manim_render()
    else:
        print("Manim setup failed!")