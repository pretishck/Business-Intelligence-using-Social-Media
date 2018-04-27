import csv
import re

inpwords = csv.reader(open('feature_incomplete.csv', 'rb'))

outwords = open('feature_list_unedited.txt','w+')
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

def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)


def getFeatureVector(word):
    
    #split tweet into words
    #replace two or more with two occurrences
    word = replaceTwoOrMore(word)
    #strip punctuation
    word = word.strip('\'"?,.')
    #check if the word stats with an alphabet
    val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
    #ignore if it is a stop word
    if(word in stopWords or val is None):
        return -1
    else:
        return word

st = open('feature_list/stopwords.txt', 'r')
stopWords = getStopWordList('feature_list/stopwords.txt')

for row in inpwords:
	word = row[0]
	count = row[1]
	word = getFeatureVector(word)
	if word != -1:
		outwords.write(word)
		outwords.write('\t')
		outwords.write(count)
		outwords.write('\n')
	else:
		continue

outwords.close()
