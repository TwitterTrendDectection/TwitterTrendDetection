import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("df_all_data6.csv", encoding = "utf-8", parse_dates = True, lineterminator = "\n")
df['created_at'] = df['created_at'].astype('datetime64[ns]')
# df.drop('id', axis = 1, inplace = True)
df.drop('text', axis = 1, inplace = True)
grouped = df.groupby('created_at')
#g = grouped.groups
df_count = grouped.count()
df_count.sort(inplace = True)
#df_count.plot(kind ='bar')
time_max = df_count.index.max()
time_min = df_count.index.min()

print time_max
print time_min