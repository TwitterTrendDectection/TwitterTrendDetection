import pandas as pd
import numpy as np

def get_time_interval(time_file):
    df = pd.read_csv('./file/' + time_file, encoding = "utf-8", parse_dates = True, lineterminator = "\n")
    df['created_at'] = df['created_at'].astype('datetime64[ns]')
    df.drop('text', axis = 1, inplace = True)
    grouped = df.groupby('created_at')
    df_count = grouped.count()
    df_count.sort(inplace = True)
    # df_count.to_csv("../../test_sorted_tweets_en2.csv")
    time_max = df_count.index.max()
    time_min = df_count.index.min()
    interval = time_max - time_min
    interval = interval / np.timedelta64(1,'h')
    return interval




if __name__ == "__main__":
    # train_file = "df_all_data.csv"
    # time = get_time_interval(train_file)
    #
    # print time
    test_file = "df_all_data.csv"
    time = get_time_interval(test_file)
    print time
