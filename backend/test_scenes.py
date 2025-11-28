from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from bernoulli import BernoulliScene
from matrix_power import MatrixPowerScene

# Test Bernoulli scene
print("Testing Bernoulli scene...")
try:
    scene1 = BernoulliScene()
    scene1.render()
    print("✅ Bernoulli scene rendered successfully")
except Exception as e:
    print(f"❌ Bernoulli scene failed: {e}")

# Test Matrix scene (needs LaTeX)
print("\nTesting Matrix scene...")
try:
    scene2 = MatrixPowerScene()
    scene2.render()
    print("✅ Matrix scene rendered successfully")
except Exception as e:
    print(f"❌ Matrix scene failed: {e}")
    print("Install LaTeX first: choco install miktex -y")