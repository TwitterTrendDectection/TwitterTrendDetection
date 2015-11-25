# __author__ = 'Yan'


import numpy as np
import lda
import lda.datasets
import csv
import re
import operator
import scipy.sparse as sparse


def engine():
    tweet_token, tweet_dict = file_reader()
    total_dict = get_dict(tweet_token)
    token_top = dict(sorted(total_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:1000])
    token_list = list(token_top.keys())
    tweet_mtx = feature_matrix(tweet_token, tweet_dict, token_list)
    topic_extract(tweet_mtx, token_list)


def topic_extract(x, vocab):
    print "Starting topic generator."
    model = lda.LDA(n_topics=1, n_iter=50, random_state=1)
    model.fit(x)  # model.fit_transform(X) is also available
    topic_word = model.topic_word_  # model.components_ also works
    n_top_words = 3
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))


def feature_matrix(review_token, review_dict, token_list):
    # map the top list token
    index_list = []
    index_list = list(range(0, 1000))
    # get the top 1000 token dict with corresponding index
    top_dict = dict(zip(token_list, index_list))
    # generate the training data matrix
    row_list = []
    col_list = []
    data_list = []
    for line_idx in range(0, len(review_token)):
        cur_dict = review_dict[line_idx]
        for key in cur_dict:
            if key in top_dict:
                row_list.append(line_idx)
                col_list.append(top_dict.get(key))
                data_list.append(cur_dict.get(key))

    train_mtx = sparse.coo_matrix((data_list, (row_list, col_list)), dtype=np.int64)
    # output = open('result/hash_test_mtx.pkl', 'wb')
    # pickle.dump(train_mtx, output)
    # output.close()
    print "Matrix generated.\n"
    return train_mtx.toarray()


def get_dict(review_token):
    token_dict = {}
    for review_cur in review_token:
        # token_list = review_cur.split(" ")
        token_list = re.sub("[^\w]", " ",  review_cur).split()
        for cur_token in token_list:
            cur_count = token_dict.get(cur_token, 0) + 1
            token_dict[cur_token] = cur_count
    # print "Finish getting token dict.\n"
    return token_dict


def file_reader():
    tweet_path = 'resources/train_text_time_en.csv'
    stop_word = stopword_reader()
    token_list = []
    dict_list = []
    count = 0
    with open(tweet_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            count += 1
            tweet = row['text']
            tweet_token, tweet_dict = tokenize(tweet, stop_word)
            token_list.append(tweet_token)
            dict_list.append(tweet_dict)
            if count == 1000:
                break
    return token_list, dict_list


def tokenize(text, stop_words):
    # save all tokens in list
    text_tokens = []
    text_dict = {}
    # CITE: discuss this expression with xiaoxul
    text = re.sub('[^\s\w]|\w*\d\w*', '', text).split()
    for token in text:
        if token not in stop_words:
            text_tokens.append(token.strip())
            num = text_dict.get(token, 0) + 1
            text_dict[token] = num
    # join all the tokens in to a single string
    str_token = ' '.join(text_tokens)
    return str_token, text_dict


def stopword_reader():
    list_path = "resources/stopword.list"
    word_set = set()
    list_file = open(list_path, 'r').read().split("\n")
    for line in list_file:
        word_set.add(line)
    return word_set

if __name__ == "__main__":
    engine()
