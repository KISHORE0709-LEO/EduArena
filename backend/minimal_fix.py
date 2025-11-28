import os
import sys

# Set FFmpeg path BEFORE any imports
backend_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(backend_dir, 'ffmpeg', 'ffmpeg-8.0.1-essentials_build', 'bin', 'ffmpeg.exe')

os.environ['FFMPEG_BINARY'] = ffmpeg_path
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_path
os.environ['PATH'] = os.path.dirname(ffmpeg_path) + ';' + os.environ.get('PATH', '')

# Import and configure Manim
import manim
manim.config.ffmpeg_executable = ffmpeg_path
manim.config.disable_caching = True
manim.config.quality = "low_quality"
manim.config.media_dir = os.path.join(backend_dir, "media")

from manim import *

class SimpleScene(Scene):
    def construct(self):
        text = Text("Working", font_size=48)
        self.add(text)

if __name__ == "__main__":
    scene = SimpleScene()
    scene.render()
    print("SUCCESS")