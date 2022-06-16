# import tweepy


# api_key = 'KTnyc1Pl66HJQvCl3UOPHa3ZO'

# api_key_secret = 'yQ58vapX2z1Bp3aRvbBYCaUY0ztroxXh8Nez3TCFoyx9fNlZQm'

# access_token = '1505281153024073730-deWWqk2ib7yh0lgfPAuCuuyeb3sexP'

# access_token_secret = 'K3QgkqF5d99XqRrkf5wLmKVUbxPV4jB5QmjIpxnRBI43P'

# bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE%2BoaQEAAAAAvnieO2DVOTah6E0EV1KlAkxE%2FxU%3D1vzatKrCR3DwG3BktLFzeHvZSvkhQRV5dXLM2W0cMZH27OTvW3'

# client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret, wait_on_rate_limit= True)

# username = 'CHAfrica_Tech'

# def follow_user(username):
#     try:
#         user_id = client.get_user(username = username).data.id
#         return client.follow_user(target_user_id=user_id)
#     except:
#         print('Invalid user')
#         quit

# def tweet_search(query):
#     return client.search_recent_tweets(query = query, max_results = 100).data



# def retweet(tweets):
#     i = 0
#     while i < len(tweets):
#         tweet = tweets[i].data
#         tweet_id = tweet.get('id')
#         client.retweet(tweet_id = tweet_id)
#         i = i + 1

# follow_user(username)
# tweets = tweet_search()
# retweet(tweets)

import tweepy

api_key = "Y4rwzfaembgiW3LhBco0SldVk"
api_key_secret = "8P794lsMVTltbgK3K2xJ4uZJIpohAwoPFRfDaxgIEyeEZF4HKC"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP%2FGaQEAAAAACVn03iqSsVzGlu8UHchcDU1aPLE%3Du6VFl4qo4kQbWJgiJyFyqqndpSdCPDz4Ar9SoPuy4aVjL2PXUB"
access_token_secret = "opCr3asJM8ssNCWYRg6PSFJNZIrBleei6IDS5TGVTvm9P"
access_token = "1505604838910009348-27CqzHepgtOCj2ZFxG87pegOD7jWwi"

#initialize a new tweepy instance
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret, wait_on_rate_limit=True)
username = "CHAfrica_tech"


def followUser(username):

    try:
        user = client.get_user(username=username).data
        client.follow_user(target_user_id=user.id)
    except:
        return 'request could not be completed'

def getUserTweets(username):
    try:
        user=client.get_user(username=username)
        return client.get_users_tweets(id=user[0].id).data
    except:
        return 'request could not be completed'

def retweet(tweet_id):
    client.retweet(tweet_id=tweet_id)


followUser(username)
user_tweets_list = getUserTweets(username)
tweets = user_tweets_list[0].data
tweet_id = tweets.get('id')
retweet(tweet_id)