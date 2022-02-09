import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []
    Balls_total = 0

    def __init__(self, **ball_colors_numbr):
        self.addContent(ball_colors_numbr)
        # print(self,self.contents)

    def addContent(self, ball_colors_numbr):
        for ball in ball_colors_numbr:
            for i in range(ball_colors_numbr[ball]):
                self.contents.append(ball)
            # print(obj,ball,"\t=" ,ball_colors_numbr[ball])
            self.Balls_total += ball_colors_numbr[ball]
        # print(self.contents)
        # print(self.Balls_total)

    def draw(self, val):
        drawn_balls = []
        if val >= len(self.contents):
            drawn_balls = copy.deepcopy(self.contents)
            self.contents.clear()
            return drawn_balls
        else:
            for i in range(val):
                index = random.randint(0, len(self.contents) - 1)  # print(index)
                drawn_balls.append(self.contents.pop(index))
        # print(drawn_balls, self.contents)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    test_hat = copy.deepcopy(hat)
    target = []
    target_total = 0
    probability = 0

    # for ball in expected_balls:
    #     for i in range(expected_balls[ball]):
    #         target.append(ball)
    #         # print(obj,ball,"\t=" ,ball_colors_numbr[ball])
    #     target_total += expected_balls[ball]
    # print("hallo", test_hat, target, target_total)

    for experiment_number in range(num_experiments):
      test_hat.contents = copy.deepcopy(hat.contents)

      test_target = expected_balls
      tmp = test_hat.draw(num_balls_drawn)
      print("experiment_number:", experiment_number, tmp)

      for ball in test_target:
        for i in range(expected_balls[ball]):
          target.append(ball)
          # print(obj,ball,"\t=" ,ball_colors_numbr[ball])
          target_total += expected_balls[ball]

    return probability
