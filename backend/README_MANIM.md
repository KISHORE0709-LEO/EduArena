# Manim Integration for EduArena

This backend integrates Manim (Mathematical Animation Engine) to convert text prompts into educational animations.

## Setup Instructions

### 1. Install System Dependencies

**Windows:**
- Install [FFmpeg](https://ffmpeg.org/download.html) and add to PATH
- Install [MiKTeX](https://miktex.org/download) for LaTeX support
- Run `install_manim.bat` to install Python dependencies

**Linux/Mac:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg texlive texlive-latex-extra texlive-fonts-extra

# macOS
brew install ffmpeg mactex

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python simple_server.py
```

The server will run on `http://localhost:8007`

## Supported Animation Types

### 1. Sorting Algorithms
- **Prompt examples:**
  - "bubble sort 5 numbers"
  - "sort the array [64, 34, 25, 12, 22]"
  - "merge sort visualization"

### 2. Vector Operations
- **Prompt examples:**
  - "vector addition with two arrows"
  - "add vectors a and b"
  - "vector mathematics visualization"

### 3. Binary Trees
- **Prompt examples:**
  - "binary search tree"
  - "tree data structure"
  - "binary tree insertion"

### 4. Mathematical Functions
- **Prompt examples:**
  - "plot sine function"
  - "quadratic equation graph"
  - "function visualization"

### 5. Basic Animations
- **Prompt examples:**
  - "explain photosynthesis"
  - "show molecular structure"
  - "demonstrate physics concept"

## API Endpoints

### POST /generate-animation
Starts animation generation process.

**Request:**
```json
{
  "prompt": "bubble sort 5 numbers"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "status": "processing",
  "message": "Animation generation started"
}
```

### GET /animation-status/{animation_id}
Check animation generation status.

**Response:**
```json
{
  "status": "completed|processing|failed",
  "video_url": "/video/animation_id.mp4",
  "prompt": "original prompt"
}
```

### GET /video/{filename}
Serve generated video files.

## Customization

### Adding New Animation Types

1. Edit `manim_generator.py`
2. Add new classification logic in `_classify_prompt()`
3. Create new scene class in `_get_scene_class()`
4. Test with appropriate prompts

### Example Custom Scene

```python
class CustomScene(Scene):
    def construct(self):
        # Your Manim animation code here
        title = Text("Custom Animation")
        self.play(Write(title))
        self.wait(2)
```

## Troubleshooting

### Common Issues

1. **FFmpeg not found:**
   - Ensure FFmpeg is installed and in system PATH
   - Restart terminal/command prompt after installation

2. **LaTeX errors:**
   - Install complete LaTeX distribution (MiKTeX/TeX Live)
   - For math-heavy animations, ensure all LaTeX packages are available

3. **Slow rendering:**
   - Manim rendering can be CPU-intensive
   - Consider using lower quality settings for faster preview
   - Adjust `config.quality` in `manim_generator.py`

4. **Memory issues:**
   - Large animations may require significant RAM
   - Consider breaking complex animations into smaller scenes

### Performance Tips

- Use `config.quality = "low_quality"` for faster development
- Limit animation duration for quicker rendering
- Use simpler geometric shapes for better performance
- Cache frequently used objects

## File Structure

```
backend/
├── manim_generator.py      # Core Manim integration
├── simple_server.py        # FastAPI server
├── requirements.txt        # Python dependencies
├── install_manim.bat      # Windows setup script
├── media/                 # Generated video output
└── README_MANIM.md        # This file
```

## Contributing

To add new animation types:

1. Study existing scene classes in `manim_generator.py`
2. Follow Manim documentation: https://docs.manim.community/
3. Test thoroughly with various prompts
4. Update classification logic accordingly

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Examples Gallery](https://docs.manim.community/en/stable/examples.html)
- [FFmpeg Download](https://ffmpeg.org/download.html)
- [MiKTeX Download](https://miktex.org/download)