from background_model import background_model
import pandas as pd
import math
import time
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
if __name__ == "__main__":

    # df = pd.read_csv()
    start = time.time()
    df = pd.read_csv("train_text_time_en.csv", encoding="utf-8", parse_dates=True, lineterminator="\n")
    df_2 = pd.read_csv("test_text_time_en.csv", encoding="utf-8", parse_dates=True, lineterminator="\n")
    threshold = 10
    print "load two dataframe: " + str(time.time() - start) #1.6s

    # df = pd.DataFrame(["There is also a corpus of instant messaging chat sessions",
    #                    "originally collected by the Naval Postgraduate School for research",
    #                    "on automatic detection of Internet predators. The corpus contains",
    #                    "over 10,000 posts, anonymized by replacing usernames with generic names of"
    #                    ], columns=['tweet_text'])
    bm = background_model(new_time_interval = 292)
    bm.read_data_frame(df)

    test_bm = background_model(new_time_interval = 1)
    test_bm.read_data_frame(df_2)

    start = time.time()

    generator = hot_words_generator(bm,test_bm,threshold)
    hot_words = generator.detect_hot_words()

    print "time to detect hot words: " + str(time.time() - start)

    start = time.time()

    f = open("hotwords.csv",'w')
    hot_words.append(u"bats\u00E0")
    for i in hot_words:
        f.write(i.encode('utf-8') + "\n")
    f.close()

    print "time to write hotwords file: " + str(time.time() - start)