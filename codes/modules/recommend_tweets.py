import numpy as np
import pickle
import pandas as pd
import csv
from random import randint

def recommend_tweets(trend_map, user_recommendation_map):
    tweets = pd.read_csv('./file/all_en_file.csv', encoding = "utf-8", parse_dates = True, lineterminator = "\n", quoting=csv.QUOTE_ALL, delimiter=',')
    res_recommendation = []
    for person in user_recommendation_map:
        print person
        # print user_recommendation_map[person]
        person_recommendation = []
        trend_list = user_recommendation_map[person]
        for trend in trend_list:
            tweet_ids = trend_map[trend][1]
            tweet_ids = list(tweet_ids)
            choose = randint(0,len(tweet_ids) - 1)
            choose_one = tweets[tweets['id'] == tweet_ids[choose]]
            print trend
            print person
            print choose_one['text']
            person_recommendation.append(choose_one['id'])

        res_recommendation.append(person_recommendation)
    return res_recommendation


if __name__ == "__main__":
    trend_map = pickle.load(open('./file/trend_group.pkl','rb'))
    user_recommendation_map = pickle.load(open('./file/user_recommendation_map.pkl','rb'))
    res = recommend_tweets(trend_map, user_recommendation_map)
    print res[0]