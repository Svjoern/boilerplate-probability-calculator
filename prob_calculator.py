import copy
import random
# Consider using the modules imported above.

class Hat:
  content = []

  def __init__(self, *args, **kwargs):
    self.addContent(args, kwargs)

  # def __init__(self, blue=0, red=0, green=0):
  #   self.blue = blue
  #   self.red = red
  #   self.green = green
    
  def addContent(self,*args, **kwargs):
    for elem in args:
      self.content.append(elem.kwargs)

  def draw(self, val):
    if val >= len(self.content):
      return self.content

    for i in range(val):
      return random.sample(self.content, val)
      # print(random.sample(self.content, val))




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass