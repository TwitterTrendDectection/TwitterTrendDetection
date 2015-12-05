from hot_words_generator import *
import pickle
from group import group_burst
from util import *
from hotwords_statistic import generate_hotword_to_tweet_dictionary
train_time_file = "train_text_time_en.csv"
train_save_model(train_time_file)

test_time_file = "test_sorted_tweets_en.csv"
test_model(test_time_file, threshold=10)

generate_hotword_to_tweet_dictionary(tweet_test_file = test_time_file, hotword_file = hotwords_file, generate_file = word_to_set_file)
group_burst(pickle_file = word_to_set_file, generate_file=generate_groupburst_file)



