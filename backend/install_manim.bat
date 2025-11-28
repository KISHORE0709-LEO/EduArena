@echo off
echo Installing Manim and dependencies...

REM Install Python dependencies
pip install -r requirements.txt

REM Install system dependencies for Manim (Windows)
echo.
echo Installing system dependencies...
echo Please ensure you have:
echo 1. FFmpeg installed and in PATH
echo 2. LaTeX distribution (MiKTeX or TeX Live) for math rendering
echo 3. Cairo and Pango libraries

echo.
echo If you don't have these, please install:
echo - FFmpeg: https://ffmpeg.org/download.html
echo - MiKTeX: https://miktex.org/download
echo.

REM Test Manim installation
echo Testing Manim installation...
python -c "import manim; print('Manim installed successfully!')"

pause