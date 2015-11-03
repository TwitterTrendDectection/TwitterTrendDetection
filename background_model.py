# from nltk.stem.lancaster import LancasterStemmer
# st = LancasterStemmer()
from preprocess_nlp import tokenize,lemmetize,remove_stop_words
from nltk.stem import WordNetLemmatizer
import pandas as pd
import time
class background_model:
    'Common base class for background model'
    def read_data_frame(self, data_frame):
        st = WordNetLemmatizer()
        data_frame['list_words'] = data_frame['tweet_text'].apply(lambda content: tokenize(content))
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: lemmetize(word_list, st))
        data_frame['list_words'] = data_frame['list_words'].apply(lambda word_list: remove_stop_words(word_list))

        start = time.time()

        series = data_frame.list_words.apply(lambda x: pd.value_counts(x)).sum(axis = 0)
        for key in series.index:
            self.background_dictionary[key] = series[key] / self.time_interval


        print "read data_frame time " + str(time.time() - start)

    def __init__(self, new_time_interval):
        self.background_dictionary = {}
        self.time_interval = new_time_interval;# default time interval is 1 hour

    def read_file(self, word_list):
        f = self.open_model_write()
        for word in word_list:
            self.add_word_count(word)
        self.write_model_to_model_file()
        self.close_model(f)
    def open_model_write(self):
        f = open("background_model.txt",'w')
        return f
    def close_model(self,f):
        f.close()

    def read_model_from_model_file(self):
        f = open("background_model.txt",'r')
        line_number = 0
        for line in f:
            if line_number == 0:
                #read time interval
                self.time_interval = int(line[:-1])
            else:
                split_line = line.split(' ')
                key = split_line[0]
                value = float(split_line[1])
                self.background_dictionary[key] = value
            line_number += 1
        f.close()

    def write_model_to_model_file(self):
        #write model from single file
        f = open("background_model.txt",'w')
        f.write(str(self.time_interval) + "\n")
        for key in self.background_dictionary:
            f.write(key + " " + str(self.background_dictionary[key]) + "\n")
        f.close()

    def get_word_count(self, word):
        #get the word's count from the model
        if word in self.background_dictionary:
            return self.background_dictionary[word]
        else:
            return 0

    def add_word_count(self, word):
        if word in self.background_dictionary:
            self.background_dictionary[word] = ((self.background_dictionary[word] * self.time_interval) + 1) * 1.0
            self.background_dictionary[word] = self.background_dictionary[word] / self.time_interval
        else:
            self.background_dictionary[word] = 1.0 / self.time_interval

def example():
    df = pd.DataFrame([], columns=['tweet_text'])
    str = "There is also a corpus of instant messaging chat sessions"
    for i in range(10):
        df.loc[i] = str

    # print df['tweet_text']

if __name__ == "__main__":
    # word_list = ['I','am','from','china','and','china','is','a','beautiful','country']
    # example()
    df = pd.DataFrame(["There is also a corpus of instant messaging chat sessions",
                       "originally collected by the Naval Postgraduate School for research",
                       "on automatic detection of Internet predators. The corpus contains",
                       "over 10,000 posts, anonymized by replacing usernames with generic names of"
                       ], columns=['tweet_text'])
    bm = background_model(new_time_interval = 4)
    bm.read_data_frame(df)

    bm.write_model_to_model_file()

    # df_2 = pd.DataFrame(["sessions corpus sessions anonymized replace replace replace"], columns=['tweet_text'])
    # test_bm = background_model(new_time_interval = 1)
    # test_bm.read_data_frame(df_2)


