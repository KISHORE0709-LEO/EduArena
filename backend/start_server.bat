@echo off
echo Starting EduArena Backend with Manim Integration...
echo.
echo Make sure you have installed:
echo 1. FFmpeg (in PATH)
echo 2. LaTeX distribution (MiKTeX)
echo 3. Python dependencies (run install_manim.bat first)
echo.
cd /d "d:\Kishore\New_project\EduArena\backend"
python simple_server.py
pause