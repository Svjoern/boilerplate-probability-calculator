import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []
    # Balls_total = 0

    def __init__(self, **ball_colors_numbr):
        self.addContent(ball_colors_numbr)
        # print("hat.contents:\t", ball_colors_numbr)

    def addContent(self, ball_colors_numbr):
        self.contents.clear()
        self.Balls_total = 0

        for ball in ball_colors_numbr:
            for i in range(ball_colors_numbr[ball]):
                self.contents.append(ball)
                # print(obj,ball,"\t=" ,ball_colors_numbr[ball])
            self.Balls_total += ball_colors_numbr[ball]
        # print(self.contents, self.Balls_total)

    def draw(self, val):
        drawn_balls = []
        if val >= len(self.contents):
            # print("return entire content")
            drawn_balls = copy.deepcopy(self.contents)
            self.contents.clear()
            # return drawn_balls
        else:
            for i in range(val):
                index = random.randint(0,len(self.contents)-1)  # print(index)
                drawn_balls.append(self.contents.pop(index))
        # print(drawn_balls, self.contents)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_balls_drawn == len(hat.contents):
        return 1.0

    test_hat = copy.deepcopy(hat)
    P = 0  # probability
    M = 0  # succesful_draws
    N = num_experiments
    target_total = 0

    for ball in expected_balls:
        # print("\nfind", ball, "ball", test_target[ball], "times \n")
        target_total += expected_balls[ball]
    # print("target_total:",target_total,"\n")

    for experiment_number in range(num_experiments):
        test_target_total = 0
        test_target = copy.deepcopy(expected_balls)  # probably directly copy it cos dictionary
        test_hat.contents = copy.deepcopy(hat.contents)     
        current_Draw = test_hat.draw(num_balls_drawn)
        # print("current_Draw",current_Draw)
        # print("test_target", test_target)
        # print("exp:",experiment_number,current_Draw, test_target)

        for ball in test_target:
            # print("\nfind", ball, "ball", test_target[ball], "times \n")
            test_target_total = test_target[ball]
            ball_ctr = 0
            for i in range(test_target[ball]):
                for current_Draw_index, current_Draw_ball in enumerate(current_Draw):
                    if current_Draw_ball == ball:
                        if ball_ctr == test_target_total:
                          break
                        current_Draw[current_Draw_index] = ""
                        ball_ctr +=1                       
        ctr=0
        for elem in current_Draw:
            if elem == "":
                ctr+=1
        if ctr >= target_total:
            M +=1
    P = M / N
    # print("M", M, "N", N)
    return P
