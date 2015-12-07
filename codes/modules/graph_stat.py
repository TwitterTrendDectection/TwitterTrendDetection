import pickle
# from background_model import background_model
from hot_words_generator import test_model
# import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go
# background_dictionary = pickle.load(open('../file/background_dictionary.pkl','r'))
# pos_tag = pickle.load(open('../file/pos_tag.pkl','r'))
# test_time_file ="test_text_time_en.csv"
# hotwords = test_model(test_time_file, threshold=10)
f = open('../../file/trend_statistic.txt','r')
dict = {}
for line in f:
    s = line.split()
    if s[0] not in dict:
        dict[s[0]] = int(s[1])
    else:
        dict[s[0]] += int(s[1])
hotwords = []
freq = []
for key in dict:
    hotwords.append(key)
    freq.append(dict[key])
# hotwords.sort(key=lambda x: x[0], reverse=True)
# hotword = []
# freq = []
# for i in hotwords:
#     hotword.append(i[1])
#     freq.append(i[0])
# # print type(pos_tag)
#
# plt.plot(hotwords, frequency)
# plt.plot([1,2,3])
py.sign_in('benji.b', '4r26wpg85l')
data = [
    go.Bar(
        x=hotwords,
        y=freq
    )
]
plot_url = py.plot(data, filename='hotwords-frequency')