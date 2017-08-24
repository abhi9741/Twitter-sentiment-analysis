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

