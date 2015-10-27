import os
import tweepy

auth = tweepy.OAuthHandler("ltmdE1M5bgvzKgOrtzrXpBBLU", "4GqOV4zS0LmgrXuu2YE4sCaPgiUnC5kFBY2bM3y1utRkDbuHnZ")
auth.set_access_token("2972025861-MaDigIstH835Ottkqk28pQynSshbyeBOtmd6R9M", "tzIKeulAqcXW9azRBF0E6OcwhXW7EcthO19EVQqrTpmhi")

api = tweepy.API(auth)

def get_tweets(id_list):
    tweets = api.statuses_lookup(id_list)
    result_string = ''
    for tweet in tweets:
        result_string += "{}\t{}\t{}\n".format(tweet.created_at, tweet.author.screen_name.encode('utf8'), tweet.text.encode('utf8'))
    return result_string
        

if __name__ == '__main__':
    count = 0
    for i in os.listdir(os.getcwd() + '/tweets2'):
        print len(i)
        if len(i) == 32:
            txt = open('./tweets2/'+i, 'r')
            out = open('./tweets2/'+i+".tsv", 'w')
            tweet_id_list = []
            for tweet_id in txt:
                if len(tweet_id) < 10:
                    continue
                (id, name, hash) = tweet_id.split("\t")
                tweet_id_list.append(id)
                if len(tweet_id_list) == 100:
                    result_string = get_tweets(tweet_id_list)
                    out.write(result_string)
                    tweet_id_list = []
                    count = count + 1
            result_string = get_tweets(tweet_id_list)
            out.write(result_string)
    print count