# import FilterTweet
from FilterTweets import *
#Support Vector Machine Classifier
import svm
from svmutil import *
from tokenizer import *


def getFeatureList(FeatureListFileName):
    #read the stopwords file and build a list
    features = []
    fp = open(FeatureListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        features.append(word)
        line = fp.readline()
    fp.close()
    return features

#Get feature Vector
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

def getSVMFeatureVectorAndLabels(tweets, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    feature_vector = []
    labels = []
    for t in tweets:
        label = 0
        map = {}
        #Initialize empty map
        for w in sortedFeatures:
            map[w] = 0

        tweet_words = t[0]
        tweet_opinion = t[1]
        #Fill the map
        for word in tweet_words:
            #process the word (remove repetitions and punctuations)
            word = replaceTwoOrMore(word)
            word = word.strip('\'"?,.')
            #set map[word] to 1 if word exists
            if word in map:
                map[word] = 1
        #end for loop
        values = map.values()
        feature_vector.append(values)
        if(tweet_opinion == '4'):
            label = 1
        elif(tweet_opinion == '0'):
            label = -1
        elif(tweet_opinion == '2'):
            label = 0
        elif(tweet_opinion == '6'):
            label = 2
        labels.append(label)
    #return the list of feature_vector and labels
    return {'feature_vector' : feature_vector, 'labels': labels}
#end

def getSVMFeatureVector(test_tweet, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    test_feature_vector = []
    label = 0
    #Initialize empty map
    for w in sortedFeatures:
       map[w] = 0
 
        #Fill the map
    for word in test_tweet:
        #process the word (remove repetitions and punctuations)
        word = replaceTwoOrMore(word)
        word = word.strip('\'"?,.')
        #set map[word] to 1 if word exists
        if word in map:
            map[word] = 1
        #end for loop
    test_values = map.values()
    test_feature_vector.append(test_values)
    '''if(tweet_opinion == '4'):
            label = 1
    elif(tweet_opinion == '0'):
            label = -1
    elif(tweet_opinion == '2'):
            label = 0
    labels.append(label)'''
    #return the list of feature_vector and labels
    return test_feature_vector
#end
featureList = getFeatureList('feature_1.txt')
#get the input
import csv
inpTweets_1 = csv.reader(open('data/Book1.csv','rb'))
tweets = []
for row in inpTweets_1:
    sentiment = row[1]
    #if sentiment == 0 or sentiment == 2 or sentiment == 4 or sentiment == 6:
      
    tweet = row[0]
    #processedTweet = word_tokenizer(re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet))
    processedTweet = processTweet(tweet)
        #for p in processedTweet:
         #   print p
    featureVector = getFeatureVector(processedTweet)
    #featureVector=getFeatureVector(processedTweet)
    #featureList.extend(featureVector) 
    tweets.append((featureVector, sentiment))
    #else:
     #   continue

#Train the classifier

result = getSVMFeatureVectorAndLabels(tweets, featureList)
problem = svm_problem(result['labels'], result['feature_vector'])
#'-q' option suppress console output
param = svm_parameter('-q')
param.kernel_type = LINEAR
classifier = svm_train(problem, param)
svm_save_model("svm_final_classifer", classifier)
classifier = svm_load_model("svm_final_classifer")

f1 = open('data/output_final_check_with_sentiment.csv', 'w')
output = csv.writer(f1, delimiter=',')
f2 = open('data/bookdata.csv', 'rb')
input_test_tweet = csv.reader(f2)
output_data = []
#Test the classifier using the test data csv file

for row in input_test_tweet:
    test_tweet = row[0]
    data = processTweet(test_tweet)
    test_feature_vector = getSVMFeatureVector(getFeatureVector(data), featureList)
    #p_labels contains the final labeling result
    p_labels, p_accs, p_vals = svm_predict([0] * len(test_feature_vector),test_feature_vector, classifier)
    print p_labels
    output_data.append((data, p_labels[0]))
output.writerows(output_data)
f1.close()
