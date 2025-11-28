import os
import subprocess
import shutil
from pathlib import Path

def test_ffmpeg():
    """Test if ffmpeg is working properly"""
    
    # Add local ffmpeg to PATH
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_paths = [
        os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin'),
        os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-master-latest-win64-gpl', 'bin'),
    ]
    
    current_path = os.environ.get('PATH', '')
    for path in ffmpeg_paths:
        if os.path.exists(path) and path not in current_path:
            current_path = f"{path};{current_path}"
    
    os.environ['PATH'] = current_path
    
    # Test ffmpeg
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("FFmpeg is working!")
            print(f"Version: {result.stdout.split()[2]}")
            return True
        else:
            print("FFmpeg failed to run")
            return False
    except Exception as e:
        print(f"FFmpeg test failed: {e}")
        return False

if __name__ == "__main__":
    test_ffmpeg()