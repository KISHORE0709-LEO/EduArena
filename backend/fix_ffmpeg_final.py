import os
import sys
import subprocess

def fix_ffmpeg_permanently():
    """Final fix for ffmpeg path issues"""
    
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
    
    # Test if ffmpeg works
    try:
        result = subprocess.run([ffmpeg_path, '-version'], capture_output=True, timeout=5)
        print(f"FFmpeg test result: {result.returncode}")
        if result.returncode != 0:
            print("FFmpeg executable has issues")
            return False
    except Exception as e:
        print(f"FFmpeg test failed: {e}")
        return False
    
    # Set all possible environment variables
    env_vars = {
        'FFMPEG_BINARY': ffmpeg_path,
        'IMAGEIO_FFMPEG_EXE': ffmpeg_path,
        'FFMPEG_EXE': ffmpeg_path,
        'PATH': f"{os.path.dirname(ffmpeg_path)};{os.environ.get('PATH', '')}"
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"Set {key} = {value}")
    
    # Import and configure manim
    try:
        import manim as mn
        
        # Direct assignment to all possible config attributes
        mn.config.ffmpeg_executable = ffmpeg_path
        
        # Patch manim internals
        import manim.utils.file_ops as file_ops
        file_ops.FFMPEG_BIN = ffmpeg_path
        
        # Patch imageio
        try:
            import imageio_ffmpeg
            imageio_ffmpeg._FFMPEG_PATH = ffmpeg_path
        except:
            pass
        
        print("All ffmpeg paths configured")
        return True
        
    except Exception as e:
        print(f"Manim configuration failed: {e}")
        return False

if __name__ == "__main__":
    fix_ffmpeg_permanently()