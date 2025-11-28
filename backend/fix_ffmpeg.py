import os
import shutil

# Copy ffmpeg to a location Python can find
backend_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_source = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')
ffmpeg_dest = os.path.join(backend_dir, 'ffmpeg.exe')

if os.path.exists(ffmpeg_source):
    shutil.copy2(ffmpeg_source, ffmpeg_dest)
    print(f"Copied ffmpeg to {ffmpeg_dest}")
    
    # Set environment
    os.environ['FFMPEG_BINARY'] = ffmpeg_dest
    os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_dest
    print("FFmpeg environment set")
else:
    print("FFmpeg source not found")