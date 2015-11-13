from background_model import background_model
import pandas as pd
import math
import time
import pickle

word_to_set = {}
hot_word_list = set()
def count(content):
    for word in content['list_words']:
        if word in hot_word_list:
            tweet_set = word_to_set.get(word)
            if tweet_set is None:
                tweet_set = set()
            tweet_set.add(content.id)
            word_to_set[word]=tweet_set

if __name__ == "__main__":
    df_2 = pd.read_csv("test_sorted_tweets_en.csv", encoding="utf-8", parse_dates=True, lineterminator="\n")
    print df_2
    test_bm = background_model(new_time_interval = 1)
    test_bm.read_data_frame(df_2)
    
    for word in open("hotwords.csv", "r"):
        hot_word_list.add(word.strip())

    df_2.apply(lambda content: count(content), axis=1)
    pickle.dump(word_to_set, open("word_to_set.pkl", "wb"))