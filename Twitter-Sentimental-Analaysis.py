import re  
import tweepy  
from textblob import TextBlob  

#This function cleans tweet(String processing)  
def clean_tweet(tweet):   
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())  

  
#This function authenticates twitter user using consumer keys, consumer secret key, access token key, access token secret key.   
def authentication():  
	consumer_key = 'r7AgkIrLENJbOlBpIwOh2px32'  
	consumer_secret = 'uPaYOsNvAxSUfTxirlTHgeQcb8HChd6Fsf7uA7tjkgtcJSbjzG'  

    access_token = '719410046174498816-zROytmN7YWAIs6evzHT9Q6sNm2Epmke'  
    access_token_secret = 'Ce328rgAdoLuylnvSzlEPiXxPQCZaC9JAa4cU47f4TOBn'  


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
	auth.set_access_token(access_token, access_token_secret)    
	return tweepy.API(auth)  
  
def tweetType(tweet):  

	if("RT " in tweet_text):  
		return "Retweet"  
	else:  
		return "Tweet"  

  
api = authentication()  


#Getting word(Keyword) from user.  

key_word = input('Enter word you want to search tweet for: ')  
  
public_tweets = api.search(key_word)  

for tweet in public_tweets:  
	print("\n\n")  
	tweet_text = clean_tweet(tweet.text)  

	tType = tweetType(tweet_text)  

	if(tType == 'Retweet'):  
		tweet_text = tweet_text.replace("RT ","")  


    
	analysis = TextBlob(tweet_text)  
	if(analysis.detect_language() != 'en' and len(tweet_text) > 3):  
		lang = analysis.detect_language()  
		try:  
			analysis.translate(from_lang=lang ,to='en')  
		except:  
			pass  

	            
	print("Tweet : ",tweet_text)  
	print()  
	print("Result of sentiment analysis : ",end="")  
	if(analysis.sentiment.polarity  > 0):  
		print("Happy")  

	elif(analysis.sentiment.polarity == 0):  
		print("Neutral")  

	else:  
		print("Sad")  
