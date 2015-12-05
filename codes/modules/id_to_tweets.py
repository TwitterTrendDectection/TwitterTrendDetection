import pickle
from util import *
import pandas as pd
from preprocess_nlp import *
import time
def id_to_tweets(test_time_file):
    group_trends = pickle.load(open('../file/' + generate_groupburst_file,'rb'))
    df_test_file = pd.read_csv('../file/' + test_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")

    res = []
    for trend_tuple in group_trends:
        id_set = trend_tuple[1]
        id_list = list(id_set)
        df_subset = df_test_file[df_test_file['id'].isin(id_list)]
        word_list = documents_to_word(df_subset)
        res.append(word_list)
    pickle.dump(res, open('../file/id_to_tweets.pkl','wb'))

def documents_to_word(data_frame):
    # list_tweets = data_frame['text'].values.tolist()
    list_tweets = data_frame['text'].apply(lambda content: remove_punctuation(content))
    list_tweets = list_tweets.apply(lambda content: tokenize(content))
    list_tweets = list_tweets.apply(lambda word_list: lowercase(word_list))
    list_tweets = list_tweets.apply(lambda word_list: remove_stop_words(word_list))

    list_tweets = list_tweets.apply(lambda word_list: stemmize(word_list))

    list_tweets = list_tweets.apply(lambda word_list: remove_words_contain_numbers(word_list))

    word_list = list_tweets.values.tolist()
    word_list = [item for sublist in word_list for item in sublist]
    return word_list

