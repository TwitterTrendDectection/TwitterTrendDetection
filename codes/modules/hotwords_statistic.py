from background_model import background_model
import pandas as pd
import pickle

word_to_set = {}
hotword_list = set()
def count(content):
    for word in content['list_words']:
        if word in hotword_list:
            tweet_set = word_to_set.get(word)
            if tweet_set is None:
                tweet_set = set()
            tweet_set.add(content.id)
            word_to_set[word]=tweet_set

def generate_hotword_to_tweets(hotword_list, tweet_test_file):
    df_2 = pd.read_csv('./file/'+tweet_test_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    test_bm = background_model(new_time_interval = 1)
    test_bm.read_data_frame(df_2)
    hotword_list = set(hotword_list)
    df_2.apply(lambda content: count(content), axis=1)
    return word_to_set

if __name__ == "__main__":
    hotword_file = "hotwords_2.pkl"
    tweet_test_file = "test_sorted_tweets_en.csv"
    generate_hotword_to_tweet_dictionary(tweet_test_file, hotword_file)
