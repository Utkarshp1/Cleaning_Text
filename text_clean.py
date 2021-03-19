import re
import stanza
from nltk.stem import WordNetLemmatizer

def process_tweet(tweet):
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove old style retweet text "QT"
    tweet = re.sub(r'^QT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    # tweet = re.sub(r'#', '', tweet)
    # tweet = re.sub("#\S+", "", tweet)
    # tweet = re.sub("@\S+", "", tweet)
    tweet = tweet.replace("#", "")
    tweet = tweet.replace("@", "")
    return tweet
  
def english_lemmatizer(tweet, nlp_en):
    doc = nlp_en(tweet)
    return " ".join([result["lemma"] for lists in doc.to_dict() for result in lists])
    
def hindi_lemmatizer(tweet, nlp_hi):
    doc = nlp_hi(tweet)
    return " ".join([result["lemma"] for lists in doc.to_dict() for result in lists])
    
def lemmatizer(review, keep_emoji=False):
    review = review.lower()           # convert to lowercase

    if keep_emoji:
        regex = re.compile('(?u)\\b\\w\\w+\\b')       # Break each sentence on the basis of punctuations, white spaces
        review = regex.findall(review)
    else:
        review = review.split()

    for pos in ["v", "n"]:
        review = [WordNetLemmatizer().lemmatize(token, pos=pos) for token in review]

    return " ".join(review)