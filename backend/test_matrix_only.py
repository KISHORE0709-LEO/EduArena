from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from matrix_power import MatrixPowerScene

# Test Matrix scene
print("Testing Matrix scene...")
try:
    scene = MatrixPowerScene()
    scene.render()
    print("SUCCESS: Matrix scene rendered")
except Exception as e:
    print(f"FAILED: Matrix scene error: {e}")
    import traceback
    traceback.print_exc()