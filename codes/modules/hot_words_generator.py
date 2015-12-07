import math
import pickle

import config
import pandas as pd
import time_explore
from background_model import background_model


class hot_words_generator:
    def __init__(self, train_model, test_model, threshold):
        self.train_model = train_model
        self.test_model = test_model
        self.threshold = threshold
    def detect_hot_words(self):
        hot_words = []
        for key in self.test_model.background_dictionary:
            Observation = self.test_model.background_dictionary[key]
            if key in self.train_model.background_dictionary:
                Evaluation = self.train_model.background_dictionary[key] / self.train_model.time_interval
            else:
                Evaluation = 0
            trend_score = math.pow((Observation - Evaluation),2) / (Evaluation + 1)
            if trend_score > self.threshold:
                hot_words.append((Observation, key))
        return hot_words

def train_save_model(train_time_file):
    df = pd.read_csv('./file/' + train_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    print "get the dataframe from train_file"
    time_interval = time_explore.get_time_interval(train_time_file)
    print "train file time interval: " + str(time_interval)
    # print "get the time interval"
    bm = background_model(new_time_interval = time_interval)
    print "initialize the background model"
    bm.read_data_frame(df)
    print "read in the dataframe"
    bm.write_model_to_model_file()
    print "write to file"


def test_model(test_time_file, threshold = 10):
    df = pd.read_csv('./file/' + test_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    time_interval = time_explore.get_time_interval(test_time_file)
    print "test file time interval: " + str(time_interval)
    if time_interval == 0:
        time_interval = 1
    test_background_model = background_model(new_time_interval = time_interval)
    test_background_model.read_data_frame(df)


    trained_background_model = background_model()
    trained_background_model.read_model_from_model_file()

    generator = hot_words_generator(trained_background_model,test_background_model,threshold)
    hotwords = generator.detect_hot_words()
    hotwords_list = write_hotwords_to_file(hotwords)

    return hotwords_list


def write_hotwords_to_file(hotwords):
    hotwords_list = []
    for hotword in hotwords:
        hotwords_list.append(hotword[1])
    # pickle.dump(hotwords_list, open('./file/' + config.hotwords_file, 'w'))
    return hotwords_list


if __name__ == "__main__":
    print "ok"
    train_time_file = "train_text_time_en.csv"
    train_save_model(train_time_file)
    test_time_file = "test_text_time_en.csv"
    test_model(test_time_file)
    hotwords = pickle.load(open('../file/hotwords_2.pkl','rb'))
    print len(hotwords)
