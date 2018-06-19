## 個人情報

import tweepy

def auth():

  # https://apps.twitter.com/ にアクセスし各種キーを取得する
  # " "内には取得した各種キーを代入する
  CK = "CONSUMER_KEY"
  CS = "CONSUMER_SECRET"
  AT = "ACCESS_TOKEN"
  AS = "ACCESS_SECRET"

  auth = tweepy.OAuthHandler(CK, CS)
  auth.set_access_token(AT, AS)

  return auth
