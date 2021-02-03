###--- IMPORTS ---###
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer


###--- GLOBAL VARIABLES ---###
positive_tweets = twitter_samples.strings(
    'positive_tweets.json')  # 5000 negative tweets
negative_tweets = twitter_samples.strings(
    'negative_tweets.json')  # 5000 positive tweets
text = twitter_samples.strings('tweets.20150430-223406.json')
# 20000 neutral tweets

tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]


###--- FUNCTIONS ---###
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence


print(lemmatize_sentence(tweet_tokens[0]))
