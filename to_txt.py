from processTweet import *
import csv

inpTweets = csv.reader(open('data/cor.csv', 'rb'))
outText = open('data/full_text.txt', 'a+')
for row in inpTweets:
	tweet = row[4]
	processed_as_txt = processTweet(tweet)
	outText.write(processed_as_txt)

outText.close()
