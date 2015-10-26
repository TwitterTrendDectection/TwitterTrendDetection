import numpy as np
import pandas as pd


df = pd.read_csv("table1000.csv")
#Index([u'tweet_unixtime', u'tweet_id', u'tweet_text', u'tweet_uid'], dtype='object')
df.drop('tweet_id', axis = 1, inplace = True)
df['tweet_unixtime'] = df['tweet_unixtime'].astype('datetime64[ns]')
df.rename(columns = {'tweet_text':'raw_context', 'tweet_uid':'uid', 'tweet_unix_time':'time'}, inplace = True)
df['new_context'] = ''
df['hashtag'] = ''
df['peopleAt'] = ''

df['new_context'] = df['raw_context'].apply(lambda x: len(x)) # replace with the real NLP preprocess function