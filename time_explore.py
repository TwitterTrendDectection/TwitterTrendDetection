import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("table50000.csv")
df['tweet_unixtime'] = df['tweet_unixtime'].astype('datetime64[ns]')
df.drop('tweet_uid', axis = 1, inplace = True)
df.drop('tweet_text', axis = 1, inplace = True)
grouped = df.groupby('tweet_unixtime')
#g = grouped.groups
df_count = grouped.count()
df_count.sort(inplace = True)
#df_count.plot(kind ='bar')
time_max = df_count.index.max()
time_min = df_count.index.min()