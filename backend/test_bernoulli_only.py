from manim_config_fix import setup_manim_environment

# Setup environment first
setup_manim_environment()

from bernoulli import BernoulliScene

# Test Bernoulli scene
print("Testing Bernoulli scene...")
try:
    scene1 = BernoulliScene()
    scene1.render()
    print("✅ Bernoulli scene rendered successfully")
except Exception as e:
    print(f"❌ Bernoulli scene failed: {e}")
    import traceback
    traceback.print_exc()