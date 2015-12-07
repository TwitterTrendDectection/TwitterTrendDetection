from modules.hot_words_generator import *
from modules.hotwords_statistic import generate_hotword_to_tweet_dictionary

from modules.group_burst import group_burst
from modules.config import *
from modules.id_to_tweets import *
from modules.personal import trend


# train_time_file = "train_text_time_en.csv"
train_time_file = "train_en_file2.csv"
train_save_model(train_time_file)

# test_time_file = "test_sorted_tweets_en.csv"
test_time_file = "test_en_file2.csv"
test_model(test_time_file, threshold=10)

generate_hotword_to_tweet_dictionary(tweet_test_file = test_time_file, hotword_file = hotwords_file, generate_file = word_to_set_file)
group_burst(pickle_file = word_to_set_file, generate_file=generate_groupburst_file)

id_to_tweets(test_time_file)
#
construct_test_file_matrix(test_time_file)
a = pickle.load(open('./file/word_dictionary_list.pkl','rb'))
print a[0]
b = pickle.load(open('./file/trend_matrix.pkl','rb'))
print b[0].shape
res = trend()