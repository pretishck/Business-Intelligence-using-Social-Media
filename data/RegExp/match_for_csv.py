import re
import csv

dell_exp = "(?:dell|@dell|inspiron|xps|studio|vostro|adamo|alienware|drac|gx620|streak|venue)"
apple_exp = "(?:apple|ipad|ipod|iphone|5s|iphone 6|mac|iwatch|air)"
inputfile = csv.reader(open('tweets1.csv','rb'))
f1 = open('dell_tweet_data.csv', 'w')
output_data_dell = csv.writer(f1, delimiter=',')
f2 = open('apple_tweet_data.csv', 'w')
output_data_apple = csv.writer(f2, delimiter=',')
output_dell = []
output_apple = []
for row in inputfile:
    tweets = row[2]
    if re.search(dell_exp, tweets):
        output_dell.append((tweets, '0'))
    elif re.search(apple_exp, tweets):
        output_apple.append((tweets, '1'))
output_data_dell.writerows(output_dell)
output_data_apple.writerows(output_apple)
