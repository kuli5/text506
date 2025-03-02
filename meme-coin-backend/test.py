# test.py
from textblob import TextBlob
text = "I love Dogecoin!"
blob = TextBlob(text)
print(blob.sentiment.polarity)  # 输出情绪得分