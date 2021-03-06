# from nltk.stem.lancaster import LancasterStemmer
# st = LancasterStemmer()
import pickle
import time

import pandas as pd
from preprocess_nlp import *

import config


class background_model:
    def read_data_frame(self, data_frame):

        start = time.time()
        data_frame['text'] = data_frame['text'].apply(lambda content: remove_retweet_prefix(content))
        print "time to remove people mention: " + str(time.time() - start)

        start = time.time()
        data_frame['text'] = data_frame['text'].apply(lambda content: remove_punctuation(content))
        print "time to remove punctuation: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['text'].apply(lambda content: tokenize(content))
        print "time to tokenize: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: lowercase(word_list))
        print "time to lowercase words in word_list: " + str(time.time() - start)

        start = time.time()

        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: remove_stop_words(word_list))
        print "time to remove stop words: " + str(time.time() - start)

        start = time.time()

        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: stemmize(word_list))
        print "time to stemmetize: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: remove_stop_words(word_list))
        print "time to remove stop words: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: remove_words_contain_numbers(word_list))
        print "time to remove words that contain numbers: " + str(time.time() - start)

        start = time.time()
        tweets_list_words = data_frame['list_words']
        for tweet_list_words in tweets_list_words:
            for word in tweet_list_words:
                if word in self.background_dictionary:
                    self.background_dictionary[word] += 1
                else:
                    self.background_dictionary[word] = 1

        print "time to generate model dictionary: " + str(time.time() - start)

    def __init__(self, new_time_interval=1):
        # default time interval is 1 hour
        self.background_dictionary = {}
        self.time_interval = new_time_interval



    def read_model_from_model_file(self):
        self.background_dictionary = pickle.load(open('./file/' + config.background_dictionary_filename, 'r'))
        self.time_interval = pickle.load(open('./file/' + config.time_interval_filename, 'r'))

    def write_model_to_model_file(self):
        pickle.dump(self.background_dictionary, open('./file/' + config.background_dictionary_filename, 'w'))
        pickle.dump(self.time_interval, open('./file/' + config.time_interval_filename, 'w'))


if __name__ == "__main__":
    df = pd.DataFrame(["RT @sdas: There is also a corpus of instant messaging chat sessions",
                       "originally collected by the Naval Postgraduate School for research",
                       "on automatic detection of Internet predators. The corpus contains",
                       "over 10,000 posts, anonymized by replacing usernames with generic names of"
                       ], columns=['text'])
    bm = background_model(new_time_interval = 4)
    bm.read_data_frame(df)

    bm.write_model_to_model_file()
    bm.read_model_from_model_file()
    for key in bm.background_dictionary:
        print key + " " + str(bm.background_dictionary[key])
