#import processTweet
from processTweet import *

#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

#Read the tweets one by one and process it
'''fp = open('data/sampleTweets.txt', 'r')
line = fp.readline()'''

st = open('data/feature_list/stopwords.txt', 'r')
stopWords = getStopWordList('data/feature_list/stopwords.txt')

'''while line:
    processedTweet = processTweet(line)
    featureVector = getFeatureVector(processedTweet)
    print featureVector
    line = fp.readline()
#end loop
fp.close()'''

#Read the tweets one by one and process it
import csv
inpTweets = csv.reader(open('data/testdata.csv', 'rb'))
featureList = []
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[5]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#endloop

featureList = list(set(featureList))
feature_file = open('data/feature_file.txt', 'w+')
for f in featureList:
    feature_file.write(f + "\n")
feature_file.close()
# Extract features from the given tweet with respect to the featurelist created

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

import nltk
# training set made using nltk apply feature

#training_set = nltk.classify.util.apply_features(extract_features, tweets)
'''for i in tweets:
    print (i)
for t_set in training_set:
    print (t_set)'''


