from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings(
    'positive_tweets.json')  # 5000 negative tweets
negative_tweets = twitter_samples.strings(
    'negative_tweets.json')  # 5000 positive tweets
text = twitter_samples.strings('tweets.20150430-223406.json')
# 20000 neutral tweets

# print(positive_tweets)
# print(negative_tweets)
# print(text)
