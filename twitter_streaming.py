from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "2496058933-ZxgyeVTRt3RaId1HXk2YADnFbmo5eBFZJhQh0Ix"
access_token_secret = "r26T72dikx8MBsXvRsuqqxejjhCInHmnLZrrVDnosqgxk"
consumer_key = "UePMYA72DkpOx5pM8MeRf17dP"
consumer_secret = "hKBMfkoRzLKkf8JBQjslWOytPWYdNeyAoyY2xwwv3h1RycQVM8"

class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		return True

	
	def on_error(self, status):
		print status


if __name__ == '__main__':
	
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	stream.filter(track=['python','javascript','ruby'])
