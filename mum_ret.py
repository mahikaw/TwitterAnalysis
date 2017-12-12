from twython import Twython
from pymongo import MongoClient
import json
import pprint
client = MongoClient('localhost', 27017)
db = client.twitter
mumbai=db.mumbai_collection



app_key = 'frEaJdpWcYQRcaYSvtmCg1uyI'
app_secret = 'xtSQzEW1jQSF74bjoHk94bP8FEUZy7TiTdkcHdv2VqcPVaUIJc'
oauth_token = "712657229174812673-ufHCP8sJr8jvj8bFgSbjXLpC8fweIZV" # from step 2
oauth_token_secret = 'gPbcmF2dc9t3xlvA4qmxpycppIanIJ5eBj27gkUzdlx78' # from step 2

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
user_input = raw_input("Enter ids separated by commas: ")

input_list = user_input.split(',')
for i in input_list:
	trends = twitter.search(q=i,result_type="mixed",count=100)
	for hashtag in trends['statuses']:
		mumbai.insert(hashtag)
		pprint.pprint(hashtag)
		