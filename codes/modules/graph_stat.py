

import plotly.plotly as py
import plotly.graph_objs as go

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

py.sign_in('benji.b', '4r26wpg85l')
data = [
    go.Bar(
        x=hotwords,
        y=freq
    )
]
plot_url = py.plot(data, filename='hotwords-frequency')