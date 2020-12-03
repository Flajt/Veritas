from six import Iterator
import tweepy
import json

class API():
    
    def __init__(self,entrypoint:str=None,number_tweets:int=20,number_followers:int=20,number_following:int=20)-> None:
        self._key=""
        self._secret=""
        self.auth = tweepy.OAuthHandler(self._key,self._secret)
        self.number_tweets = number_tweets
        self.number_followers = number_followers
        self.number_following = number_following
        #self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        self.entrypoint=entrypoint# entrypoint for graph, starts from here
    
    

    def getNewPosts(self,user:str=None,json:bool=False):
        if user==None:
            if json:
                return self._jsonifyTweets(self._pretifyTweets(self.api.user_timeline(id=self.entrypoint,tweet_mode="extended")))
            else:
                return self._pretifyTweets(self.api.user_timeline(id=self.entrypoint,tweet_mode="extended"))
            
        else:
            if json:
                return self._jsonifyTweets(self._pretifyTweets(self.api.user_timeline(id=user,tweet_mode="extended")))
            else: 
                return self._pretifyTweets(self.api.user_timeline(id=user,tweet_mode="extended"))
    
    def getAllPosts(self,user:str=None,retweets:str="-")->Iterator:
        """
        Gets all posts using pagination

        Params:
            user: Name/ID of the user to querry for -> str
            
        """
        if user==None:
            return tweepy.Cursor(self.api.user_timeline,id=user,tweet_mode="extended").pages()
        else:
            return tweepy.Cursor(self.api.user_timeline,id=user,tweet_mode="extended").pages()

    def _jsonifyTweets(self,tweets:list) -> list:
        """Converts string to json"""
        jsonified = []
        for i in tweets:
            jsonified.append(json.loads(i))
        return jsonified

    def _pretifyTweets(self,tweets:list)-> list:
        """
        Function which returns a pretified version of the input
        """
        jsonstorage = []
        for tweet in tweets:
            jsonstr = json.dumps(tweet._json) #converts json to string
            prepedJson = json.loads(jsonstr)
            jsonstorage.append(json.dumps(prepedJson,sort_keys=True,indent=4))
        return jsonstorage
    
    def getFriends(self,user,friends_count:int=20)-> list:
        """ Get's the persons the user is following"""
        return self._pretifyTweets(self.api.friends(id=user,count=friends_count))#TODO: Set count to the number of friends we can get from the user object

    def getFollowers(self,user:str,follower_count:int=20)-> list:
        """Get's the followers of the user"""
        return self._pretifyTweets(self.api.followers(id=user,count=follower_count))#TODO: Set count to the number of followers we can get from the user object

    def getFollowerCount(self,user=None) -> int:
        """Get's the number of followers that a user has"""
        if user!=None:
            return self._jsonifyTweets([user])[0]["followers_count"]
        else:
            return self.api.get_user(id=self.entrypoint)._json["followers_count"]
    
