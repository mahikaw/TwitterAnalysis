from flask import Flask,render_template
from pymongo import MongoClient
import json
import operator
# import userjson
client = MongoClient()
db = client.twitter
delhi=db.delhi_collections
mumbai=db.mumbai_collection

app = Flask(__name__)


mumbai_tweet_locations={}
mumbai_hastgas={}
trending={}
retweet_mumbai_count=0
tweet_mumbai_count=0
mumbai_favorite_count=0
image_count=0
video_count=0
text_count=0
for i in mumbai.find({}):

        tweet_mumbai_count+=1
        mumbai_favorite_count=mumbai_favorite_count+i['favorite_count']
        if "media" in i['entities']:
                if i['entities']['media'][0]['type']=="photo":
                        image_count+=1
                elif    i['entities']['media'][0]['type']=="video":
                        video_count+=1
        if "extended_tweet" in i:
                if "media" in i['extended_tweet']:
                        if i['extended_tweet']['media'][0]['type']=="photo":
                                image_count+=1
                        elif    i['entities']['media'][0]['type']=="video":
                                video_count+=1
        else:
                text_count+=1
        if "retweeted_status" in i:
                retweet_mumbai_count+=i['retweeted_status']['retweet_count']

                mumbai_favorite_count=mumbai_favorite_count+i['retweeted_status']['favorite_count']

        if i['user']['time_zone'] not in mumbai_tweet_locations and i['user']['time_zone']!="null":

                mumbai_tweet_locations[i['user']['time_zone']]=1
        else:
                mumbai_tweet_locations[i['user']['time_zone']]=mumbai_tweet_locations[i['user']['time_zone']]+1

        if i['entities']['hashtags']!=[]:
                access_hash=i['entities']['hashtags'][0]['text']
                if access_hash not in trending:
                        trending[access_hash]=1
                else:
                        trending[access_hash]=trending[access_hash]+1
c=sorted(trending, key=trending.get,reverse=True)
d=[]
flag=0
i=0
delhi_tweet_locations={}
retweet_delhi_count=0
delhi_favorite_count=0
tweet_delhi_count=0





for i in delhi.find({}):

        tweet_delhi_count+=1
        delhi_favorite_count=delhi_favorite_count+i['favorite_count']
        if "media" in i['entities']:
                if i['entities']['media'][0]['type']=="photo":
                        image_count+=1
                elif    i['entities']['media'][0]['type']=="video":
                        video_count+=1
        if "extended_tweet" in i:
                if "media" in i['extended_tweet']:
                        if i['extended_tweet']['media'][0]['type']=="photo":
                                image_count+=1
                        elif    i['entities']['media'][0]['type']=="video":
                                video_count+=1
        else:
                text_count+=1
        if "retweeted_status" in i:
                retweet_delhi_count+=i['retweeted_status']['retweet_count']

                delhi_favorite_count=delhi_favorite_count+i['retweeted_status']['favorite_count']

        if i['user']['time_zone'] not in delhi_tweet_locations and i['user']['time_zone']!="null":

                delhi_tweet_locations[i['user']['time_zone']]=1
        else:
                delhi_tweet_locations[i['user']['time_zone']]=delhi_tweet_locations[i['user']['time_zone']]+1

        if i['entities']['hashtags']!=[]:
                access_hash=i['entities']['hashtags'][0]['text']
                if access_hash not in trending:
                        trending[access_hash]=1
                else:
                        trending[access_hash]=trending[access_hash]+1
tweets_Total=tweet_mumbai_count+tweet_delhi_count

retweet_total=retweet_delhi_count+retweet_mumbai_count

print(">>>>>>>>"+str(retweet_delhi_count)+"  "+str(tweet_delhi_count))

a=sorted(trending.items(), key=operator.itemgetter(1),reverse=True)
trends=[]

for x in xrange(1,11):
    try:
        s=a[x][0].encode()
    except UnicodeEncodeError:
        pass
    trends.append(s)
mumbai_location_json=json.dumps(mumbai_tweet_locations)
delhi_location_json=json.dumps(delhi_tweet_locations)
# print mumbai_tweet_locations
# print "\n"
# print delhi_tweet_locations


@app.route('/')
def hello_world():
    return render_template("index.html",
        tweet_arvind_count=tweet_delhi_count,
        tweet_modi_count=tweet_mumbai_count,
        tweets_Total=tweets_Total,
        retweet_total=retweet_total,
        favorite_count=mumbai_favorite_count+delhi_favorite_count,
        mumbai_favorite_count=mumbai_favorite_count,
        delhi_favorite_count=delhi_favorite_count,
        trending=d,
        del_json=delhi_location_json,
        mum_json=mumbai_location_json,
        image_count=image_count,
        text_count=text_count,
        trends=trends,
        video_count=video_count)

    
if __name__ == '__main__':
        app.run(host='35.197.138.123:5000',debug=True,use_reloader=True)








