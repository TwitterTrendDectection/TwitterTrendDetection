
import glob
import pandas as pd
from preprocess_nlp import *
import numpy as np

from collections import Counter
from scipy.sparse import coo_matrix
import lda
import pickle




def preprocess(df):
    list_tweets = df['text'].apply(lambda content: remove_punctuation(content))
    list_tweets = list_tweets.apply(lambda content: tokenize(content))
    list_tweets = list_tweets.apply(lambda word_list: lowercase(word_list))
    list_tweets = list_tweets.apply(lambda word_list: remove_stop_words(word_list))
    list_tweets = list_tweets.apply(lambda word_list: stemmize(word_list))
    list_tweets = list_tweets.apply(lambda word_list: remove_words_contain_numbers(word_list))

    text_list = list_tweets.values.tolist()
    token_list = []
    for x in text_list:
        token_list.append(Counter(x))
    #pprint.pprint(text_list)
    word_list = [item for sublist in text_list for item in sublist]
    return token_list, word_list

def generate_token_matrix(token_list, word_list):
    m = len(token_list)
    n = len(word_list)
    index_list = range(n)
    d = dict(zip(word_list, index_list))
    row_list = []
    col_list = []
    data_list = []
    for idx in range(m):
        cur = token_list[idx]
        for x in cur:
            row_list.append(idx)
            col_list.append(d[x])
            data_list.append(cur[x])
    token_matrix = coo_matrix((data_list, (row_list, col_list)), shape = (m, n), dtype = np.int64)
    return token_matrix

def topics(token_matrix, word_list):
    res = []
    #n_topics = token_matrix.shape[0]/100
    n_topics = 1
    model = lda.LDA(n_topics, n_iter = 50, random_state = 1)
    model.fit(token_matrix)  # model.fit_transform(X) is also available
    topic_word = model.topic_word_  # model.components_ also works
    n_top_words = 20
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(word_list)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        res.append(topic_words.tolist())
        print(u'Topic {}: {}'.format(i, ' '.join(topic_words)))
    return res


def generate_personal_interest(folder_path):
    csv_list = glob.glob(folder_path+'/*.csv')
    user_topic_map = {}
    for x in csv_list:
        df = pd.read_csv(x, encoding = 'utf-8')
        token_list, word_list = preprocess(df)
        token_matrix = generate_token_matrix(token_list, word_list)
        t = topics(token_matrix, word_list)
        user_topic_map[x] = t

    return user_topic_map


def generate_trend_topic(token_matrix_list, dict_list):
    res = []
    for x in xrange(len(dict_list)):
        topic = topics(token_matrix_list[x], dict_list[x])
        res.append(topic)
    return res


def generate_user_recommendation(user_topic_map, trend_topic_map):
    user_recommendation_map = {}
    for user_entry in user_topic_map:
        topic_list = reduce(lambda x,y: x+y,user_topic_map[user_entry])
        topic_set = set(topic_list)
        user_recommendation_map[user_entry] = []
        for index,trend_topic in enumerate(trend_topic_map):
            if len(set(trend_topic[0]).intersection(set(topic_set))) > 0:
                user_recommendation_map[user_entry].append(index);
                
    return user_recommendation_map

if __name__ == "__main__":
    # generate_personal_interest('./file/personal/')
    # trend_words_list = pickle.load(open('./file/word_dictionary_list.pkl', 'rb'))
    # token_matrix_list = pickle.load(open('./file/trend_matrix.pkl', 'rb'))
    # res = generate_trend_topic(token_matrix_list, trend_words_list)
    # generate_user_recommendation(user_topic_map, trend_topic_map)
    user_topic_map = pickle.load(open('./file/user_topic_map.pkl','rb'))
    trend_topic_map = pickle.load(open('./file/trend_topic_map.pkl','rb'))
    print generate_user_recommendation(user_topic_map, trend_topic_map)
