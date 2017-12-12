from flask import Flask,render_template
from pymongo import MongoClient
import json
client = MongoClient()
db = client.twitter
delhi=db.delhi_collections
mumbai=db.mumbai_collection

result_mumbai={}
result_delhi={}

nodes_mumbai=[]
nodes_delhi=[]

links_mumbai=[]
links_delhi=[]

for i in delhi.find({}):
	#group 1
	temp1={}
	temp1['id']=i['user']['screen_name']
	temp1['group']=1
	if temp1['id'] not in nodes_delhi:
		nodes_delhi.append(temp1)
	if i['retweeted']:
		#group 2
		# for x in xrange(1,i['retweet_count']+1):
		temp2={}
		temp1={}

		temp2['source']=i['user']['screen_name']
		temp2['value']=10
		temp2['target']=i['retweeted_status']['user']['screen_name']
		links_delhi.append(temp2)

		temp1['id']=i['retweeted_status']['user']['screen_name']
		temp1['group']=2
		if temp1['id'] not in nodes_delhi:
			nodes_delhi.append(temp1)

		# print "retweet"
		# print i['retweeted']
		# print "\n"

	if i['in_reply_to_screen_name']:
		#group 3
		temp2={}
		temp1={}

		temp2['source']=i['user']['screen_name']
		temp2['value']=10
		temp2['target']=i['in_reply_to_screen_name']
		links_delhi.append(temp2)

		temp1['id']=i['in_reply_to_screen_name']
		temp1['group']=3
		if temp1['id'] not in nodes_delhi:
			nodes_delhi.append(temp1)

		# print "reply"
		# print i['in_reply_to_screen_name']
		# print "\n"

	if i['entities']['user_mentions']!='None' and i['entities']['user_mentions']:
		#group 4
		for x in i['entities']['user_mentions']:
			temp2={}
			temp1={}

			temp2['source']=i['user']['screen_name']
			temp2['value']=10
			temp2['target']=x['screen_name']
			links_delhi.append(temp2)

			temp1['id']=x['screen_name']
			temp1['group']=4
			if temp1['id'] not in nodes_delhi:
				nodes_delhi.append(temp1)

		# print "mention"
		# print i['entities']['user_mentions']
		# print "\n"

for i in mumbai.find({}):
	#group 1
	temp1={}
	temp1['id']=i['user']['screen_name']
	temp1['group']=1
	if temp1['id'] not in nodes_delhi:
		nodes_delhi.append(temp1)
	if i['retweeted']:
		#group 2
		# for x in xrange(1,i['retweet_count']+1):
		temp2={}
		temp1={}

		temp2['source']=i['user']['screen_name']
		temp2['value']=10
		temp2['target']=i['retweeted_status']['user']['screen_name']
		links_delhi.append(temp2)

		temp1['id']=i['retweeted_status']['user']['screen_name']
		temp1['group']=2
		if temp1['id'] not in nodes_delhi:
			nodes_delhi.append(temp1)

		# print "retweet"
		# print i['retweeted']
		# print "\n"

	if i['in_reply_to_screen_name']:
		#group 3
		temp2={}
		temp1={}

		temp2['source']=i['user']['screen_name']
		temp2['value']=10
		temp2['target']=i['in_reply_to_screen_name']
		links_delhi.append(temp2)

		temp1['id']=i['in_reply_to_screen_name']
		temp1['group']=3
		if temp1['id'] not in nodes_delhi:
			nodes_delhi.append(temp1)

		# print "reply"
		# print i['in_reply_to_screen_name']
		# print "\n"

	if i['entities']['user_mentions']!='None' and i['entities']['user_mentions']:
		#group 4
		for x in i['entities']['user_mentions']:
			temp2={}
			temp1={}

			temp2['source']=i['user']['screen_name']
			temp2['value']=10
			temp2['target']=x['screen_name']
			links_delhi.append(temp2)

			temp1['id']=x['screen_name']
			temp1['group']=4
			if temp1['id'] not in nodes_delhi:
				nodes_delhi.append(temp1)

		# print "mention"
		# print i['entities']['user_mentions']
		# print "\n"


result_delhi['nodes']=nodes_delhi
result_delhi['links']=links_delhi

result_json=json.dumps(result_delhi)
fl_mum=open("/static/users.json","w")
fl_mum.write(mumbai_location_json)












