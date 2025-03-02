# AI驱动的Meme币分析工具开发文档
## 项目目标
开发一个基于AI的Web工具，用于分析meme币的社交媒体情绪和链上交易数据，帮助用户识别趋势。

## 技术栈
- 前端：React
- 后端：Flask (Python)
- AI：TextBlob (情绪分析), Scikit-learn (趋势预测)
- 数据源：X API, CoinGecko API

## 开发步骤
### 1. 环境搭建
- 安装Node.js和Python。
- 创建项目文件夹：`meme-coin-frontend` 和 `meme-coin-backend`。

### 2. 数据获取
- **X情绪数据**：
  ```python
  import tweepy
  auth = tweepy.OAuthHandler("your_api_key", "your_api_secret")
  api = tweepy.API(auth)
  tweets = api.search_tweets(q="DOGE", count=100)