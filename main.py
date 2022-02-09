 # This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
# prob_calculator.random.seed(1337)
hat = prob_calculator.Hat(blue=4, red=2, green=6)

# print("num_balls_drawn=4", "num_experiments=1000")
# hat = prob_calculator.Hat(blue=3,red=2,green=6)
# expected_balls={"blue":2,"green":1}
# num_balls_drawn=4
# num_experiments=1000

# print("expected_balls:\t",expected_balls)
# probability = prob_calculator.experiment(hat, expected_balls, num_balls_drawn, num_experiments)
# print("Probability:", probability, "expected = 0.272")

# print(hat.draw(6))

print("expected_balls:  {'blue': 2, 'red': 1}")
probability = prob_calculator.experiment(hat,{"blue": 2,"red": 1},11,10) 
    # num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
# main(module='test_module', exit=False)
