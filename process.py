from tokenizer import *
import re
import csv

stopWords = []

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

#stopWords = getStopWordList('data/feature_list/stopwords.txt')


#inpTweets = csv.reader(open('data/cor.csv', 'rb'))
inpTweets = open('data/strings_combined.txt', 'rb')
outText = open('data/test_new.txt', 'w+')
for line in inpTweets:
	tweets = word_tokenizer(re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',line))
	for word in tweets:
		outText.write(word)
		outText.write(' ')


outText.close()