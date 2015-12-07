import langid
import pandas as pd
import re

import numpy as np
import csv
from datetime import datetime
def language_identify(content):
    threshold = 0.5
    if content == "":
        return ''
    tuples = langid.classify(content)
    if tuples[0] == 'en' and float(tuples[1]) > threshold:
        return 'en'
    else:
        return tuples[0]


def count_letters(word):
    return len(word) - word.count(' ')


def filter_question_mark(content):
    threshold = 0.3
    count_question = content.count('?')
    count_all = count_letters(content)
    if count_question * 1.0 / count_all > threshold:
        return ""
    else:
        return content


def count_en(content):
    if content == "en":
        return 1


def extract_link(list_text):
    print "start extracting link.\n"
    link_group = []
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    for text in list_text:
        match = re.search(regex, text)
        if match:
            print "succeed.\n"
            print match.group() + "\n"
            link_group.append(match.group())
        else:
            print "failed.\n"
    return link_group



def process_only_english(time_file):
    df = pd.read_csv('./file/' + time_file, encoding = "utf-8", parse_dates = True, lineterminator = "\n")

    df['created_at'] = df['created_at'].astype('datetime64[ns]')

    df.sort(inplace = True)
    df.to_csv('./file/test_all_file.csv',encoding = 'utf-8')


def read_csv():
    import json
    import glob as gb
    csv_file_names = gb.glob("./file/csv_file/*.csv")
    # print json_file_names[0]
    data = []
    # frames = [df1, df2, df3]
    frames = []
    # In [5]: result = pd.concat(frames)

    for file_name in csv_file_names:
        # print file_name
        df = pd.read_csv(file_name, encoding = "utf-8", parse_dates = True, lineterminator = "\n", quoting=csv.QUOTE_ALL, delimiter=',')
        df['created_at'] = df['created_at'].astype('datetime64[ns]')
        df = df[df['lang'] == 'en']
        frames.append(df)


    data = pd.concat(frames)

    # grouped = data.groupby('created_at')
    # df_count = grouped.count()
    data.sort_values(by = 'created_at',inplace = True)
    data.to_csv('./file/all_en_file.csv',encoding = 'utf-8',index=False, index_label=False)
    # return data

def get_specific_time(specific_day, specific_start_hour, specific_end_hour):
    df = pd.read_csv('./file/all_en_file.csv', encoding = "utf-8", parse_dates = True, lineterminator = "\n", quoting=csv.QUOTE_ALL, delimiter=',')
    count = len(df.index) - 1
    sum = 0
    frames = []
    start = 0
    end = count
    while count >= 0:
        # print count
        row = df.iloc[count]
        time = row['created_at']
        time = str(time)
        spli = time.split()
        date = spli[0].split('-')
        # date = date[0]
        # print date
        d = datetime(int(date[0]), int(date[1]),int(date[2]))
        if d < specific_day:
            break
        elif d == specific_day:
            # print int(spli[1][0:2])
            if int(spli[1][0:2]) >= int(specific_start_hour) and int(spli[1][0:2]) < int(specific_end_hour):
                sum += 1
            if int(spli[1][0:2]) < int(specific_start_hour):
                start = count
                print "start" + str(start)
                break
            if int(spli[1][0:2]) >= int(specific_end_hour):
                end = count
                print "end" + str(end)


        count = count - 1
    print start
    print end
    df_train = df[:count]
    # df_test = pd.concat(frames)
    df_test = df[start+1:end]
    df_train.to_csv('./file/train_en_file2.csv',encoding = 'utf-8',index=False, index_label=False)
    df_test.to_csv('./file/test_en_file2.csv',encoding = 'utf-8',index=False, index_label=False)
    print sum

if __name__ == "__main__":
    # process_only_english('df_all_data.csv')
    # read_csv()
    # specific_day = '03-08'
    specific_start_hour = '19'
    specific_end_hour = '23'
    get_specific_time(datetime(2011,3,7),specific_start_hour,specific_end_hour)