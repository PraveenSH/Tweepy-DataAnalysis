import json 
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = './programming_language.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
for i in range(len(tweets)):
	print str(tweets['text'][i])
