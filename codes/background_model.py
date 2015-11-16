# from nltk.stem.lancaster import LancasterStemmer
# st = LancasterStemmer()
from preprocess_nlp import tokenize,lemmetize,remove_stop_words,lowercase,remove_punctuation, remove_words_contain_numbers
from nltk.stem import WordNetLemmatizer
import pandas as pd
import time
class background_model:
    def read_data_frame(self, data_frame, visited = {}):
        start = time.time()
        wnl = WordNetLemmatizer()

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
        for i, row in data_frame.iterrows():
            word_list = row['list_words']
            # print i
            data_frame.set_value(i, 'list_words',lemmetize(word_list, wnl, visited))
        print "time to lemmetize: " + str(time.time() - start)

        self.write_pos_tag_words(visited)

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

    def write_pos_tag_words(self, visited, pos_tag_filename = "pos_tag.txt"):
        f = open('./file/' + pos_tag_filename,'w')
        for key in visited:
            f.write(key + " " + str(visited[key]) + " " + "\n")
        f.close()

    def get_pos_tag_words(self, pos_tag_filename = "pos_tag.txt"):
        visited = {}
        f = open('./file/' + pos_tag_filename, 'r')
        for line in f:
            str = line.split()
            visited[str[0]] = int(str[1])
        f.close()

    def __init__(self, new_time_interval = 1):
        self.background_dictionary = {}
        self.time_interval = new_time_interval;# default time interval is 1 hour

    def read_file(self, word_list):
        f = self.open_model_write()
        for word in word_list:
            self.add_word_count(word)
        self.write_model_to_model_file()
        self.close_model(f)
    def open_model_write(self, model_filename = "background_model.txt"):
        f = open('./file/' + model_filename,'w')
        return f
    def close_model(self,f):
        f.close()

    def read_model_from_model_file(self, model_filename = "background_model.txt"):
        f = open('./file/' + model_filename,'r')
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
        f = open('./file/' + "background_model.txt",'w')
        f.write(str(self.time_interval) + "\n")
        key = u'\u201c'
        self.background_dictionary[key] = 100
        for key in self.background_dictionary:
            f.write(key.encode('utf-8') + " " + str(self.background_dictionary[key]) + "\n")
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
    df = pd.DataFrame([], columns=['text'])
    str = "There is also a corpus of instant messaging chat sessions"
    for i in range(10):
        df.loc[i] = str

    # print df['tweet_text']

if __name__ == "__main__":
    df = pd.DataFrame(["There is also a corpus of instant messaging chat sessions",
                       "originally collected by the Naval Postgraduate School for research",
                       "on automatic detection of Internet predators. The corpus contains",
                       "over 10,000 posts, anonymized by replacing usernames with generic names of"
                       ], columns=['text'])
    bm = background_model(new_time_interval = 4)
    bm.read_data_frame(df)

    bm.write_model_to_model_file()
    bm.read_model_from_model_file('background_model.txt')
    for key in bm.background_dictionary:
        print key + " " + str(bm.background_dictionary[key])


