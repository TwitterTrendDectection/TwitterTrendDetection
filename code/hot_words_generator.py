import math
import time

import pandas as pd

from background_model import background_model
import time_explore


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
                Evaluation = self.train_model.background_dictionary[key]
            else:
                Evaluation = 0
            trend_score = math.pow((Observation - Evaluation),2) / (Evaluation + 1)
            if trend_score > self.threshold:
                    hot_words.append(key)
        return hot_words

def train_save_model(train_file, train_time_file):
    df = pd.read_csv('./file/' + train_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    time_interval = time_explore.get_time_interval(train_time_file)
    bm = background_model(new_time_interval = time_interval)
    bm.read_data_frame(df)
    bm.write_model_to_model_file()


def test_model(test_time_file, trained_model = "../file/background_model.txt", threshold = 10):
    df = pd.read_csv('./file/' + test_time_file, encoding="utf-8", parse_dates=True, lineterminator="\n")
    time_interval = time_explore.get_time_interval(test_time_file)
    test_background_model = background_model(new_time_interval = time_interval)
    test_background_model.read_data_frame(df)

    trained_background_model = background_model()
    trained_background_model.read_model_from_model_file(trained_model)
    generator = hot_words_generator(trained_background_model,test_background_model,threshold)
    hotwords = generator.detect_hot_words()
    return hotwords

def write_hotwords_to_file(hotwords, generated_file = "hotwords.csv"):
    f = open("./file/" + generated_file,'w')
    for i in hotwords:
        if len(i) != 1:
            f.write(i.encode('utf-8') + "\n")
    f.close()
if __name__ == "__main__":
    test_file = "test_time_example.csv"
    test_time_file = "test_time_example.csv"
    hotwords = test_model(test_time_file)
    write_hotwords_to_file(hotwords)



