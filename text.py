import random

class Sashimi:

  def __init__(self, number):
    self.number = number

    self.normal = []
    self.special = []
    self.rea = []
    self.super_special = []
    self.pre_text = []


  def open_text(self):
    with open("./texts/normal.txt", "r") as f:
            self.normal = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/special.txt", "r") as f:
            self.special = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/rea.txt", "r") as f:
            self.rea = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/super_special.txt", "r") as f:
            self.super_special = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/pre_text.txt", "r") as f:
            self.pre_text = [line.replace("\n", "") for line in f.readlines()]

  def rate(self):
    N = random.randrange(1000)

    if N == 343: flag = "ss"
    elif N < 50: flag = "s"
    elif N < 100: flag = "r"
    else: flag = "n"
    
    return flag

  def make_tweet(self,flag):
    if flag == "n":
      text = random.choice(self.pre_text) + random.choice(self.normal)
        
    elif flag == "r":
      text = random.choice(self.rea)
        
    elif flag == "s":
      text = random.choice(self.special)          
        
    elif flag == "ss":
      text = random.choice(self.super_special)
    
    return text

  def result(self):

    self.open_text()

    tweet_text = "\n"

    if self.number > 1:
      tweet_text += "【お寿司10連】"

      for i in range(1, self.number + 1):
        tweet_text += "\n" + str(i) + ". "
        tweet_text += self.make_tweet(self.rate())

    else:
      tweet_text += self.make_tweet(self.rate())

    return tweet_text
