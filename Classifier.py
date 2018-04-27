# import FilterTweet
from FilterTweets import *
#Support Vector Machine Classifier
import svm
from svmutil import *

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

#return the feature vector for tweet

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
    #return the list of feature_vector
    return test_feature_vector

classifier = svm_load_model("svm_classifer")

f1 = open('data/output_tweet_with_sentiment.csv', 'w')
output = csv.writer(f1, delimiter=',')
f2 = open('data/test_tweet_data.csv', 'rb')
input_test_tweet = csv.reader(f2)
output_data = []
#Test the classifier using the test data csv file

for row in input_test_tweet:
    test_tweet = row[0]
    data = processTweet(test_tweet)
    test_feature_vector = getSVMFeatureVector(getFeatureVector(data), getFeatureList('data/feature_file.txt'))
    #p_labels contains the final labeling result
    p_labels, p_accs, p_vals = svm_predict([0] * len(test_feature_vector),test_feature_vector, classifier)
    print p_labels
    output_data.append((data, p_labels[0]))
output.writerows(output_data)
f1.close()
