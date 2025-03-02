import os
import tweepy
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv() 
# 读取 API Key 和 Token 
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# 连接 Twitter API

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# 获取速率限制状态
rate_limit_status = api.rate_limit_status()
print(rate_limit_status)
# 搜索推文示例
# response = client.search_recent_tweets(query="Dogecoin", max_results=10)

# for tweet in response.data:
#     print(tweet.text)
