import pickle
from config import *
import pandas as pd
from preprocess_nlp import *
import numpy as np
import scipy.sparse as sparse


def documents_to_word(data_frame):
    list_tweets = word_list_preprocess(data_frame)
    word_list = list_tweets.values.tolist()
    word_list = [item for sublist in word_list for item in sublist]
    return word_list


def id_to_tweets(test_time_file):
    group_trends = pickle.load(open('./file/' + generate_groupburst_file,'rb'))
    df_test_file = pd.read_csv('./file/' + test_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")

    res = []
    for trend_tuple in group_trends:
        id_set = trend_tuple[1]
        id_list = list(id_set)
        df_subset = df_test_file[df_test_file['id'].isin(id_list)]
        word_list = documents_to_word(df_subset)
        res.append(word_list)
    print res[0]
    pickle.dump(res, open('./file/id_to_tweets.pkl','wb'))


def construct_test_file_matrix(test_time_file):
    # id_to_tweets is file contains all words for each trend

    # then for each trend, we want to construct list of trend matrix where each element is a matrix
    # also keep a list of list where sublist contains

    id_to_tweets = pickle.load(open('./file/id_to_tweets.pkl','rb'))
    df_test_file = pd.read_csv('./file/' + test_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    group_trends = pickle.load(open('./file/' + generate_groupburst_file,'rb'))
    ith = 0
    res_list_matrix = []
    list_word_vector = []
    list_word_dictionary = []
    # count = 0
    for trend_tuple in group_trends:
        id_set = trend_tuple[1]
        id_list = list(id_set)
        df_subset = df_test_file[df_test_file['id'].isin(id_list)]
        df_subset = word_list_preprocess(df_subset)
        #the dictionary will not contain stop words
        list_word_in_trend = id_to_tweets[ith]
        word_dictionary,dict_vector = build_dictionary(list_word_in_trend)
        if ith == 0:
            print df_subset
        m_trend = build_matrix(df_subset, word_dictionary)

        res_list_matrix.append(m_trend)
        list_word_vector.append(dict_vector)
        list_word_dictionary.append(word_dictionary)

        ith += 1
    # print count
    pickle.dump(res_list_matrix, open('./file/trend_matrix.pkl','wb'))
    pickle.dump(list_word_vector, open('./file/word_dictionary_list.pkl','wb'))


def build_matrix(df, word_dictionary):
    ith_row = 0
    row_list = []
    col_list = []
    data_list = []
    for row in df:
        for word in row:
            if word in word_dictionary:
                row_list.append(ith_row)
                col_list.append(word_dictionary[word])
                data_list.append(1)
        ith_row += 1
    res_matrix = sparse.coo_matrix((data_list, (row_list,col_list)), dtype=np.int64)
    return res_matrix


def build_dictionary(list_word_in_trend):
    dict = {}
    dict_vector = []
    loc = 0
    for word in list_word_in_trend:
        if word not in dict:
            dict[word] = loc
            loc += 1
            dict_vector.append(word)
    return dict,dict_vector


def word_list_preprocess(data_frame):
    list_tweets = data_frame['text'].apply(lambda content: remove_punctuation(content))
    list_tweets = list_tweets.apply(lambda content: tokenize(content))
    list_tweets = list_tweets.apply(lambda word_list: lowercase(word_list))
    list_tweets = list_tweets.apply(lambda word_list: remove_stop_words(word_list))
    list_tweets = list_tweets.apply(lambda word_list: stemmize(word_list))
    list_tweets = list_tweets.apply(lambda word_list: remove_words_contain_numbers(word_list))
    return list_tweets

# if __name__ == "__main__":
    # id_to_tweets('test_sorted_tweets_en.csv')
    # construct_test_file_matrix('../file/test_sorted_tweets_en.csv')
