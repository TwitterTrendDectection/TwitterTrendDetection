import os
import tweepy
import time

auth = tweepy.OAuthHandler("ltmdE1M5bgvzKgOrtzrXpBBLU", "4GqOV4zS0LmgrXuu2YE4sCaPgiUnC5kFBY2bM3y1utRkDbuHnZ")
auth.set_access_token("2972025861-MaDigIstH835Ottkqk28pQynSshbyeBOtmd6R9M", "tzIKeulAqcXW9azRBF0E6OcwhXW7EcthO19EVQqrTpmhi")

class MyModelParser(tweepy.parsers.ModelParser):
    def parse(self, method, payload):
        # result = super(tweepy.parsers.ModelParser, self).parse(method, payload)
        # result._payload = payload
        # print payload
        return payload

api = tweepy.API(auth, parser=MyModelParser())

def get_tweets(id_list):
    if len(id_list) < 1:
        return ''
    tweets = api.statuses_lookup(id_list,include_entities=True)
    return tweets+"\n"
        

if __name__ == '__main__':
    count = 0
    for i in os.listdir(os.getcwd() + '/tweets'):
        print len(i)
        if len(i) == 32:
            txt = open('./tweets/'+i, 'r')
            out = open('./tweets/'+i+".json", 'w')
            tweet_id_list = []
            for tweet_id in txt:
                if len(tweet_id) < 10:
                    continue
                (id, name, hash) = tweet_id.split("\t")
                tweet_id_list.append(id)
                if len(tweet_id_list) == 100:
                    result_string = get_tweets(tweet_id_list)
                    time.sleep(16)
                    out.write(result_string)
                    tweet_id_list = []
                    count = count + 1
            result_string = get_tweets(tweet_id_list)
            out.write(result_string)
    print count