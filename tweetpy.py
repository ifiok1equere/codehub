import tweepy


api_key = 'KTnyc1Pl66HJQvCl3UOPHa3ZO'

api_key_secret = 'yQ58vapX2z1Bp3aRvbBYCaUY0ztroxXh8Nez3TCFoyx9fNlZQm'

access_token = '1505281153024073730-deWWqk2ib7yh0lgfPAuCuuyeb3sexP'

access_token_secret = 'K3QgkqF5d99XqRrkf5wLmKVUbxPV4jB5QmjIpxnRBI43P'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE%2BoaQEAAAAAvnieO2DVOTah6E0EV1KlAkxE%2FxU%3D1vzatKrCR3DwG3BktLFzeHvZSvkhQRV5dXLM2W0cMZH27OTvW3'


# client_id = 'V3BWQTdiZFN0V0JTYXVVOGtuakM6MTpjaQ'

# client_secret = 'gX2y99lATRAhrN3wLu50lbaYTdnRv-wuLFs-wGyEnKXN-mO_jV'

#initialize a new tweepy instance

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret, wait_on_rate_limit= True)
sleep_on_rate_limit = False
user = client.get_user(username = 'equereifiok').data

print(user.name, user.username, user.id)


followers_count = client.get_users_followers(id = user.id).data

#function that returns the number of followers of a specific handle
def follower_count(username):
    user_id = client.get_user(username = username).data.id
    followers = client.get_users_followers(id = user_id).data
    return followers[0], len(followers)
    #return len(followers)

#function that returns the list of followers of a specific handle
def get_followers_list(username):
    user_id = client.get_user(username = username).data.id
    follower_list = followers_count = client.get_users_followers(id = user_id).data
    return follower_list

username = 'CHAfrica_Tech'
follower_count = follower_count(username)
follower_list = get_followers_list(username)

# print(f'The username {username} has {follower_count} followers which are:', follower_list)

# userName = 'equereifiok'
# follower_count2 = follower_count(userName)

#Funcrtion to follow a user
def follow_user(username):
    try:
        user_id = client.get_user(username = username).data.id
        return client.follow_user(target_user_id=user_id)
    except:
        print('Invalid user')
    
follow_user(username = follower_list[3])


def tweet_search(query):
    return client.search_recent_tweets(query = query, max_results = 1000).data

tweets = tweet_search(query = 'ethereum')
print(tweets)

def retweet(tweets):
    i = 0
    while i < len(tweets):
        tweet = tweets[i].data
        tweet_id = tweet.get('id')
        client.retweet(tweet_id = tweet_id)
        i = i + 1
    
retweet(tweets)
