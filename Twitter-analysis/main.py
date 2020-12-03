import api
import time
api = api.API(entrypoint="realdonaldtrump",number_followers=10,number_following=10,number_tweets=10)
import math
#posts=api.getNewPosts()
#readable=api._pretifyTweets(posts)
#print(f"Number of tweets: {len(readable)}")

#friends=api.getFriends("realdonaldtrump")
#print(api._jsonifyTweets([friends[1]])[0])
#followers=api.getFollowers("realdonaldtrump")
#print(f"follower: {api._jsonifyTweets(followers)[0]['screen_name']}")
#print("_--------------------------------------")
#follower_count=api.getFollowerCount(user=followers[0])
#print(follower_count)
#print(follower_count["followers_count"])

def getInfo(friends_counter:int=3,entrypoint:str="realdonaldtrump",verbose:bool=True)-> list:
    friends_counter=3#number of friends to get more info on
    #speed = friends_counter * math.factorial(friends_counter)#e.g. 2*2! = 4
    speed = friends_counter
    followersMap = {}# stores person and their followers
    follower_class_storage={}# stores name and their json data
    followers = api.getFollowers(user=entrypoint,follower_count=friends_counter)
    ret = api._jsonifyTweets(followers)
    followersMap["realdonaldtrump"]= [i["screen_name"]for i in ret]
    try:
        for i in range(0,friends_counter):
            key = list(followersMap.keys())[-1]
            values = list(followersMap.values())[-1]
            if verbose:
                print(f"Map: {followersMap}")
                print(f"Key: {key}, values: {values}")
            for get_num_friends in range(friends_counter,0,-1):
                print(get_num_friends)
                for friend in values:
                    followers = api.getFollowers(user=friend,follower_count=get_num_friends)
                    ret = api._jsonifyTweets(followers)
                    followersMap[key] = [i["screen_name"]for i in ret]
                    follower_class_storage[key] = ret
    except Exception as e:
        if verbose:
            print(f"Error:{e}")
        else:
            pass
    return [followersMap,follower_class_storage]

print(getInfo()[0])