## リプライの内容を用意する

import random

class Sashimi:

  def __init__(self, number):

    # 10連の時は10、そうじゃない時は1
    # いずれはn連(1 <= n <= 10)に対応したい
    self.number = number

    self.normal = []
    self.special = []
    self.rea = []
    self.super_special = []
    self.pre_text = []

  # それぞれのファイルを配列に格納
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

  # 1つ1つの結果を作る
  def result(self):
    
    #ランダムに数字を選んで、対応するファイルから結果を作ってる感じ
    N = random.randrange(1000)

    if N == 343:
      text = random.choice(self.super_special)
    elif N < 50:
      text = random.choice(self.rea)
    elif N < 100:
      text = random.choice(self.special)
    else:
      text = random.choice(self.pre_text) + random.choice(self.normal)
    
    return text

  # ツイート内容を作る
  def make_tweet(self):

    self.open_text()

    tweet_text = "\n"

    # 10連の時
    if self.number > 1:

      tweet_text += "【お寿司10連ガチャ】"

      # 10回繰り返す
      for i in range(1, self.number + 1):
        tweet_text += "\n" + str(i) + ". "
        tweet_text += self.result()

    # 10連じゃない時
    else:
      tweet_text += self.result()

    return tweet_text
