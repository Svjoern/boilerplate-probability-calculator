 # This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
prob_calculator.random.seed(1337)
hat = prob_calculator.Hat(blue=4, red=2, green=6)

# print(hat.draw(6))

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    # num_experiments=3000)
    num_experiments=3)
print("Probability:", probability)

# Run unit tests automatically
# main(module='test_module', exit=False)
