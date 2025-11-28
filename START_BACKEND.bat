@echo off
echo Starting EduArena Backend Server...
cd backend
pip install flask flask-cors
python web_server.py
pause