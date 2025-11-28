import os
import sys
import subprocess
import shutil
from pathlib import Path

def setup_manim_environment():
    """Setup proper Manim environment with all required system files"""
    
    # Get absolute paths
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
    
    # Try alternative ffmpeg path if first doesn't exist
    if not os.path.exists(ffmpeg_path):
        ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-master-latest-win64-gpl', 'bin', 'ffmpeg.exe')
    
    # Verify ffmpeg exists
    if not os.path.exists(ffmpeg_path):
        print(f"FFmpeg not found at: {ffmpeg_path}")
        print("Available FFmpeg locations:")
        for root, dirs, files in os.walk(os.path.join(backend_dir, 'ffmpeg')):
            if 'ffmpeg.exe' in files:
                print(f"  Found: {os.path.join(root, 'ffmpeg.exe')}")
        return False
    
    # Set ALL possible ffmpeg environment variables
    ffmpeg_dir = os.path.dirname(ffmpeg_path)
    env_vars = {
        'FFMPEG_BINARY': ffmpeg_path,
        'IMAGEIO_FFMPEG_EXE': ffmpeg_path,
        'FFMPEG_EXE': ffmpeg_path,
        'MANIM_DISABLE_CACHING': 'True',
        'MANIM_VERBOSITY': 'WARNING',
        'PATH': f"{ffmpeg_dir};{os.environ.get('PATH', '')}"
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
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
        
        # Force all ffmpeg configurations - CRITICAL FIX
        mn.config.ffmpeg_executable = ffmpeg_path
        
        # Test FFmpeg before proceeding
        try:
            result = subprocess.run([ffmpeg_path, '-version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                print(f"FFmpeg test failed: {result.stderr}")
                return False
            print(f"FFmpeg working: {result.stdout.split()[2]}")
        except Exception as e:
            print(f"FFmpeg test error: {e}")
            return False
        
        # Patch manim internals
        try:
            import manim.utils.file_ops as file_ops
            file_ops.FFMPEG_BIN = ffmpeg_path
        except:
            pass
        
        # Patch manim internals
        try:
            import manim.utils.file_ops as file_ops
            file_ops.FFMPEG_BIN = ffmpeg_path
        except:
            pass
        
        # Patch imageio
        try:
            import imageio_ffmpeg
            imageio_ffmpeg._FFMPEG_PATH = ffmpeg_path
        except:
            pass
        
        # Set working directory
        os.chdir(backend_dir)
        
        print("Manim environment configured successfully")
        print(f"FFmpeg path: {ffmpeg_path}")
        return True
        
    except ImportError:
        print("Manim not installed. Install with: pip install manim")
        return False
    except Exception as e:
        print(f"Error configuring Manim: {e}")
        return False

def check_system_dependencies():
    """Check and report on required system dependencies"""
    
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    local_ffmpeg = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
    
    dependencies = {
        'python': sys.executable,
        'ffmpeg': local_ffmpeg if os.path.exists(local_ffmpeg) else shutil.which('ffmpeg'),
        'latex': shutil.which('latex') or shutil.which('pdflatex'),
        'magick': shutil.which('magick') or shutil.which('convert'),
    }
    
    print("System Dependencies Check:")
    for dep, path in dependencies.items():
        status = "Found" if path else "Missing"
        if dep == 'ffmpeg' and path == local_ffmpeg:
            print(f"  {dep}: {status} (local) {path}")
        else:
            print(f"  {dep}: {status} {path or ''}")
    
    # FFmpeg is required, others are optional for basic functionality
    return dependencies['python'] and dependencies['ffmpeg']

def install_missing_dependencies():
    """Attempt to install missing dependencies"""
    
    print("Attempting to install missing dependencies...")
    
    # Try to install ffmpeg via chocolatey if available
    try:
        subprocess.run(['choco', 'install', 'ffmpeg', '-y'], 
                      capture_output=True, check=False, timeout=300)
    except:
        pass
    
    # Try to install ImageMagick
    try:
        subprocess.run(['choco', 'install', 'imagemagick', '-y'], 
                      capture_output=True, check=False, timeout=300)
    except:
        pass
    
    print("Dependency installation attempted")

if __name__ == "__main__":
    print("Setting up Manim environment...")
    
    # Check dependencies first
    deps_ok = check_system_dependencies()
    
    if not deps_ok:
        print("Some dependencies are missing. Attempting to install...")
        install_missing_dependencies()
    
    # Setup environment
    setup_success = setup_manim_environment()
    
    if setup_success:
        print("Manim environment setup completed successfully!")
    else:
        print("Manim environment setup failed!")