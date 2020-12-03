import sys
from nlpBackend import Veritas # needs to be renamed later, it contains my experiments on how to convert text into questions (currently quite useless XD)
from questions import QuestionParser
#import sacremoses
#import fastBPE
sys.path.insert(1, "./Twitter-analysis/")#To access my Twitter api, for development
from api import API# Import Twitter api
import pprint# for a better overiew
from modelApi import ModelApi# Should be the wrapper for the model. currently not working
sentence:str="Hubby and I are working with @RudyGiulianion @realDonaldTrumplegal election fight. Go to @Parler to read, facts @Twitter won’t let me tell you. Court filings start next week. Had to interview witnesses, and draft Declarations to make sure all facts accurate."
#sentence:str = "Donald and I have a nice day. We will have to go upstairs." # This one and the above are example sentences to convert into questions, for testing
path="src/output/"
#m:Model = Model()# Should have been the model. 
n:Veritas = Veritas()# init Class for question parsing
#q:QuestionParser = QuestionParser()# Just an experiment, it's useless
# add path of Twitter analysis tool to Path so python can import from there
#api:API = API(number_tweets=1)# Set's the number of tweets to revice with each pull
#posts:list = api.getNewPosts(user="realDonaldTrump",json=True)# Would get posts from Donald Trump, currently not used, maybe later for testing my project
#ret:list = n.extractQuestions(posts[0]["full_text"])# Should in theory extract questions, is depreciated before really used
#post = api._pretifyTweets(posts)# would pretify tweets in a better to read style
#sprint(m.loadhub())# One of my experiments to load the model via torch hub, 
#ret:list = n.extractSentences(posts[0]["retweeted_status"]["full_text"])# would be used to split tweet into sentences

ret:list = n.extractSentences(sentence)#extracts sentences from the test string
#print(ret)
#pprint.PrettyPrinter().pprint(ret)
ret:dict=n.tokenParser(ret)# tokenizes sentences and stores them into a dictionary according to each sentence
pprint.PrettyPrinter().pprint(ret)# For better reading 
print(n.convertToQuestion(ret))# Should convert to question, but fails.... hardcoding seems quite a dumb idea
#question:str = q.englishParser(ret)
#print(f"> {question}")
#pprint.PrettyPrinter().pprint(sentence)
#print(n.pagerank(sentence))


#m = ModelApi()
