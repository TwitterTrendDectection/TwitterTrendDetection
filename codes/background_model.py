# from nltk.stem.lancaster import LancasterStemmer
# st = LancasterStemmer()
from preprocess_nlp import *
from nltk.stem import WordNetLemmatizer
import pandas as pd
import time
import pickle
import util
class background_model:
    def read_data_frame(self, data_frame):

        # wnl = WordNetLemmatizer()

        start = time.time()
        data_frame['text'] = data_frame['text'].apply(lambda content: remove_punctuation(content))
        print "time to remove punctuation: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['text'].apply(lambda content: tokenize(content))
        print "time to tokenize: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: remove_stop_words(word_list))
        print "time to remove stop words: " + str(time.time() - start)

        start = time.time()
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: lowercase(word_list))
        print "time to lowercase words in word_list: " + str(time.time() - start)

        start = time.time()
        # for i, row in data_frame.iterrows():
        #     if i % 100 == 0:
        #         print i
        #     word_list = row['list_words']
        #     data_frame.set_value(i, 'list_words',lemmetize(word_list, wnl, self.visited))
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: stemmize(word_list))
        print "time to stemmetize: " + str(time.time() - start)

        # self.write_pos_tag_words()

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

    # def write_pos_tag_words(self):
    #
    #     pickle.dump(self.visited, open('../file/' + util.pos_tag_filename,'w'))
    #
    # def get_pos_tag_words(self):
    #
    #     self.pos_tag = pickle.load(open('../file/' + util.pos_tag_filename,'r'))

    def __init__(self, new_time_interval = 1):
        self.background_dictionary = {}
        self.time_interval = new_time_interval# default time interval is 1 hour
        # self.visited = {}
    # def read_file(self, word_list):
        # f = self.open_model_write()
        # for word in word_list:
        #     self.add_word_count(word)
        # self.write_model_to_model_file()
        # self.close_model(f)
    # def open_model_write(self, ):
    #     f = open('./file/' + util.model_filename,'w')
    #     return f
    # def close_model(self,f):
    #     f.close()

    def read_model_from_model_file(self):

        self.background_dictionary = pickle.load(open('../file/' + util.background_dictionary_filename,'r'))
        self.time_interval = pickle.load(open('../file/' + util.time_interval_filename,'r'))

    def write_model_to_model_file(self):

        pickle.dump(self.background_dictionary, open('../file/' + util.background_dictionary_filename,'w'))
        pickle.dump(self.time_interval, open('../file/' + util.time_interval_filename,'w'))


if __name__ == "__main__":
    df = pd.DataFrame(["There is also a corpus of instant messaging chat sessions",
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


