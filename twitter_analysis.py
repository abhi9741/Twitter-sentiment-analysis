import tweepy as t   #this is the module that we use to access/operate twitter api
import re            #re stands for regular exppression operations , we will use this for text manipulation
from tweepy import OAuthHandler as ah

# from textblob import TextBlob
ck='bISf1uYdfepj8VvpdmIf0G2fF'      #ck stands for consumer secret
cs='xcCvvdxBqGpTQvsWc0CxXwAT8r51gvcFPnmu94U4cqwUMOUR9t'  #cs stands for consumer secret
at='890939453534908418-FyLPz2yT7J9speCvrdwAWuaFPTARA8H'  #at stands for acess token
ats='YVrScxouBU6aa1q57SSxfnxRG70D6oqNlZFHK0v6iykbY'    #ats stands for acess token secret

auth=ah(ck,cs)     #auth stands for authorisation
auth.set_access_token(at,ats)
api=t.API(auth)

#for finding the countries/places available for finding trends
trends = api.trends_available()
for trend in trends:
    print trend

# for finding trends at a current place
trends_at_a_place=api.trends_place(2295414)


# trends_at_a_place is a list with only one element in it, which is a dict  
trendsp=trends_at_a_place
data = trendsp[0]

# get  the trends
trends = data['trends']

#get the name from each trend
names = [trend['name'] for trend in trends]

# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)


#findingtwets with a particular word
results = api.search(q="Mahanati")

for result in results:
     print result.text

#for searching tweets with a particular query

public_tweets = api.search('Mahanati')
i=0
for i in range(0,3):
for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     print("")
     i=i+1


query = 'python'
max_tweets = 10
searched_tweets = [status for status in t.Cursor(api.search, q=query).items(max_tweets)]
for tweet in searched_tweets :
     print (tweet.text)
query = 'python'
max_tweets = 14
searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        print "error , following query cannot be searched at current time"   # depending on TweepError.code, one may want to retry or wait
        print "the error code forthe above error is:"
        print e

        break
for tweet in searched_tweets:
    tt=tweet.text
    ttbag=re.split(r"(\s+)",tt)
    tt1=ttbag[0]
    

    if (tt1=="RT"):
        abhi=5

    else:
        print tt
        


