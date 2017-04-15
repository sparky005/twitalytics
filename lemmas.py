from textblob import TextBlob

def split_into_lemmas(tweet):
    tweet = tweet.lower()
    words = TextBlob(tweet).words
    # get lemma
    return [word.lemma for word in words]
