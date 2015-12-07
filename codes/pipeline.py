from modules.hot_words_generator import train_save_model,test_model
from modules.hotwords_statistic import generate_hotword_to_tweets

from modules.group_burst import group_burst
from modules.config import *

from modules.trend_to_tweets import construct_test_file_matrix, generate_trend_to_tweets
from modules.personalize import generate_trend_topic, generate_personal_interest, generate_user_recommendation
import pickle
train_time_file = "train_en_file2.csv"
train_save_model(train_time_file)

test_time_file = "test_en_file2.csv"
hotword_list = test_model(test_time_file, threshold=10)
hotword_to_tweets = generate_hotword_to_tweets(hotword_list, tweet_test_file = test_time_file)
trend_groups = group_burst(hotword_to_tweets)
trend_to_tweets = generate_trend_to_tweets(trend_groups, test_time_file)
test_token_matrix, trend_words_list = construct_test_file_matrix(test_time_file, 
                                        trend_to_tweets, trend_groups)
user_topic_map = generate_personal_interest('./file/personal/')

trend_topic_map = generate_trend_topic(test_token_matrix, trend_words_list)
print 'trend_topic_map-------------------'
print trend_topic_map
print 'trend_topic_map-------------------'
pickle.dump(user_topic_map, open('./file/user_topic_map.pkl','wb'))
pickle.dump(trend_topic_map, open('./file/trend_topic_map.pkl','wb'))
user_recommendation_map = generate_user_recommendation(user_topic_map, trend_topic_map)
