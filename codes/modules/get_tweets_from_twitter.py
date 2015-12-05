import os
import tweepy
import time
from tweepy import TweepError

auth = tweepy.OAuthHandler("ltmdE1M5bgvzKgOrtzrXpBBLU", "4GqOV4zS0LmgrXuu2YE4sCaPgiUnC5kFBY2bM3y1utRkDbuHnZ")
auth.set_access_token("2972025861-MaDigIstH835Ottkqk28pQynSshbyeBOtmd6R9M", "tzIKeulAqcXW9azRBF0E6OcwhXW7EcthO19EVQqrTpmhi")

class MyModelParser(tweepy.parsers.ModelParser):
    def parse(self, method, payload):
        result = super(tweepy.parsers.ModelParser, self).parse(method, payload)
        # result._payload = payload
        return (result, payload)

api = tweepy.API(auth, parser=MyModelParser())

def get_tweets(id_list):
    if len(id_list) < 1:
        return ''
    try:
        tweets = api.statuses_lookup(id_list,include_entities=True)
    except TweepError as e:
        print e.response.status
    return tweets+"\n"


def batch_retrive_tweets_by_id():
    count = 0
    for i in os.listdir(os.getcwd() + '/tweets'):
        print len(i)
        if len(i) == 32:
            txt = open('../tweets/'+i, 'r')
            out = open('../tweets/'+i+".json", 'w')
            tweet_id_list = []
            for tweet_id in txt:
                if len(tweet_id) < 10:
                    continue
                (id, name, hash) = tweet_id.split("\t")
                tweet_id_list.append(id)
                if len(tweet_id_list) == 100:
                    result_string = get_tweets(tweet_id_list)
                    time.sleep(16)
                    out.write(result_string.encode("utf8"))
                    tweet_id_list = []
                    count = count + 1
            result_string = get_tweets(tweet_id_list)
            out.write(result_string.encode("utf8"))
    print count


def retrive_single_batch_by_screen_name(screen_name, max_id=None):
    try:
        tweets, payload = api.user_timeline(screen_name, count=200, max_id=max_id)
    except TweepError as e:
        print e.response.status
    return tweets, payload


def retrive_tweets_by_screen_name(screen_name):
    out = open("../data/{}.json".format(screen_name), 'w')
    print "Retriving tweets for {}".format(screen_name)
    count = 0
    tweets, payload = retrive_single_batch_by_screen_name(screen_name)
    print count
    while len(tweets) > 10:
        tweets, payload = retrive_single_batch_by_screen_name(screen_name, tweets[-1]["id"])
        out.write(payload.encode("utf8"))
        out.write("\n")
        print count
        print tweets[-1]["id"]
        count += len(tweets)
    out.close()

if __name__ == '__main__':
    retrive_tweets_by_screen_name("JayZClassicBars")
