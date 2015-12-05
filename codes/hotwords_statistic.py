from background_model import background_model
import pandas as pd
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

def generate_hotword_to_tweet_dictionary(tweet_test_file, hotword_file, generate_file):
    df_2 = pd.read_csv('../file/'+tweet_test_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    test_bm = background_model(new_time_interval = 1)
    test_bm.read_data_frame(df_2)

    # for word in open('./file/' + hotword_file, "r"):
    for word in pickle.load(open('../file/' + hotword_file, 'rb')):
        hot_word_list.add(word.strip())

    df_2.apply(lambda content: count(content), axis=1)
    pickle.dump(word_to_set, open(generate_file, "wb"))

if __name__ == "__main__":
    hotword_file = "hotwords_2.pkl"
    tweet_test_file = "test_sorted_tweets_en.csv"
    generate_hotword_to_tweet_dictionary(tweet_test_file, hotword_file)