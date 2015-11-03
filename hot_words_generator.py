from background_model import background_model
import pandas as pd
import math
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
    df = pd.DataFrame(["There is also a corpus of instant messaging chat sessions",
                       "originally collected by the Naval Postgraduate School for research",
                       "on automatic detection of Internet predators. The corpus contains",
                       "over 10,000 posts, anonymized by replacing usernames with generic names of"
                       ], columns=['tweet_text'])
    bm = background_model(new_time_interval = 4)
    bm.read_data_frame(df)

    df_2 = pd.DataFrame(["sessions corpus sessions anonymized replace replace replace"], columns=['tweet_text'])
    test_bm = background_model(new_time_interval = 1)
    test_bm.read_data_frame(df_2)

    generator = hot_words_generator(bm,test_bm,1)
    hot_words = generator.detect_hot_words()
    print hot_words