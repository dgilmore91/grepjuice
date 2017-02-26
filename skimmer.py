import tweepy
import tweetcleaner

consumer_key = "JQqbWnRCHpqS5SO4xwW24LaEf"
consumer_secret = "0w0NlM3MYTdVtSMEGIPv3jZmSHdSaC2yoMVss2E63aEs6RODQn"

access_token = "24718990-SL9sxLaLCmoabMTo2eGvgFWz5xIOc3PkrD2OhwXPu"
access_token_secret = "jyrkeYZov3crvbo9nEYooEbPm9qWeQVDQZRJRTZb21oLL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searchResults = api.search(
    q="british ? AND -filter:retweets", lang="en", count=100)
textArray = []

for tweet in searchResults:
    textArray.append(tweet.text.encode("utf-8") + "\n")

with open("./search_results.txt", "a") as searchResultsFile:
    for tweetText in textArray:
        cleanedTweet = tweetcleaner.cleanTweet(tweetText, ['http', '@', '#'])
        searchResultsFile.write(str(cleanedTweet))

print ("Number of tweets: " + str(len(searchResults)))
