from tweepy.streaming import StreamListener
from tweepy.streaming import Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import datetime
from datetime import timedelta
import random
import text

# https://apps.twitter.com/ にアクセスし各種キーを取得する
# " "内には取得した各種キーを代入する
CK="CONSUMER_KEY"
CS="CONSUMER_SECRET"
AT="ACCESS_TOKEN"
AS="ACCESS_SECRET"

auth = OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = API(auth)

# 起動時のメッセージ
start = "起動！\n" + \
    "[ " + str(datetime.now().strftime('%Y/%m/%d %H:%M')) + " ]"
print(start)

class Listener(StreamListener):
    # 特定の文字列に対してリプを返す処理
    def on_status(self, status):
        tweet_Text = status.text

        # いいねする
        if "お寿司" in tweet_Text and not(str(status.user.screen_name) == "my_screen_name"):
          api.create_favorite(status.id)
          print(status.user.name + " @" + str(status.user.screen_name))
          print(tweet_Text)
          print("- - - - - - - - - - - ")

        if (not status.retweeted) and ("RT @" not in tweet_Text):
            if ("お寿司" in tweet_Text and "ガチャ" in status.text) and "【お寿司10連】" not in status.text:
              tweet = "@" + str(status.user.screen_name) + " "

              if "@" in tweet_Text and " " in tweet_Text[tweet_Text.index("@"):tweet_Text.index("@")+17]:
                    for i in range(tweet_Text.index("@"),len(tweet_Text)):
                        tweet += tweet_Text[i]
                        if tweet_Text[i] == " " and not(tweet_Text[i+1] == "@"): break

              if "10連" in tweet_Text:
                sashimi = text.Sashimi(10)
              else:
                sashimi = text.Sashimi(1)

              tweet += sashimi.result()

              api.update_status(tweet, status.id)  # ツイート！
              print("-> " + tweet)
              print("-------------------")

        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('落ちた…＞＜')
        return True

listener = Listener()
stream = Stream(auth, listener, secure=True)
stream.userstream()
