from manim_config_fix import setup_manim_environment

# Setup environment
setup_manim_environment()

from bernoulli_fixed import BernoulliScene
from matrix_fixed import MatrixPowerScene

print("Generating Bernoulli video...")
scene1 = BernoulliScene()
scene1.render()

print("Generating Matrix video...")
scene2 = MatrixPowerScene()
scene2.render()

print("Videos generated in media/videos/480p15/")
print("- BernoulliScene.mp4")
print("- MatrixPowerScene.mp4")