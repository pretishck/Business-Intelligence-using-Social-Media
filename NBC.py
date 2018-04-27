# import FilterTweets
from FilterTweets import *
# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = 'I am so badly hurt'
#processedTestTweet = processTweet(testTweet)
print ("Output:")
print NBClassifier.classify(extract_features(getFeatureVector(processTweet(testTweet))))
#print NBClassifier.show_most_informative_features(60)
