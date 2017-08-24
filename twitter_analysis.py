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




