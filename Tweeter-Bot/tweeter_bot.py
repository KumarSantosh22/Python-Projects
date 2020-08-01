import tweepy
import time

auth = tweepy.OAuthHandler('<your api key here>', '<your api secret key>')
auth.set_access_token('<your access token>', '<your access token secret>')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print(follower.screen_name)

search = "Santosh"
numberOfTweets = 2

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
