import os
import glob
import pandas as pd
from preprocess_nlp import *
import numpy as np
import pprint
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
    #pprint.pprint(word_list)
    word_set = set(word_list)
    return token_list, word_set

def generateMatrix(token_list, word_set):
    m = len(token_list)
    n = len(word_set)
    word_list = list(word_set)
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
    mtx = coo_matrix((data_list, (row_list, col_list)), shape = (m, n), dtype = np.int64)
    return mtx

def topics(mtx, word_set):
    res = []
    #n_topics = mtx.shape[0]/100
    n_topics = 2
    model = lda.LDA(n_topics, n_iter = 50, random_state = 1)
    model.fit(mtx)  # model.fit_transform(X) is also available
    topic_word = model.topic_word_  # model.components_ also works
    n_top_words = 5
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(list(word_set))[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        res.append(topic_words.tolist())
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    return res

def main():
    print os.getcwd()
    csv_list = glob.glob('../../file/personal/*.csv')
    res = {}
    for x in csv_list:
        print x
        df = pd.read_csv(x, encoding = 'utf-8')
        token_list, word_set = preprocess(df)
        mtx = generateMatrix(token_list, word_set)
        print mtx.shape
        t = topics(mtx, word_set)
        res[x] = t
    pickle.dump(res, open('../../file/personal.pkl', 'wb'))
    return

def trend():
    res = []
    dict_list = pickle.load(open('../../file/word_dictionary_list.pkl', 'rb'))
    mtx_list = pickle.load(open('../../file/trend_matrix.pkl', 'rb'))
    for x in xrange(len(dict_list)):
        res.append(topics(mtx_list[x], dict_list[x]))

    return res

if __name__ == "__main__":
    #main()
    res = trend()
    print len(res)




