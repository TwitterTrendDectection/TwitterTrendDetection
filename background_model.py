# from nltk.stem.lancaster import LancasterStemmer
# st = LancasterStemmer()

class background_model:
    'Common base class for background model'

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
            return -1

    def add_word_count(self, word):
        if word in self.background_dictionary:
            self.background_dictionary[word] = ((self.background_dictionary[word] * self.time_interval) + 1) * 1.0
            self.background_dictionary[word] = self.background_dictionary[word] * 1.0 / self.time_interval
        else:
            self.background_dictionary[word] = 1.0 / self.time_interval

if __name__ == "__main__":
    word_list = ['I','am','from','china','and','china','is','a','beautiful','country']
    bm = background_model(new_time_interval = 2)
    bm.read_file(word_list)

    bm.read_model_from_model_file()
    print bm.get_word_count("and")
    bm.add_word_count("and")
    print bm.get_word_count("and")
    bm.add_word_count("and")
    print bm.get_word_count("and")
    bm.add_word_count("and")
    print bm.get_word_count("and")
    bm.add_word_count("china")
    print bm.get_word_count("china")
    import nltk
    nltk.download()