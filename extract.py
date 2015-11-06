# *****__author__ = 'Yan'*****


import pandas as pd
import glob as gb
import json
import csv


# read json files into pandas
def pandas_json():
    json_file_names = gb.glob("parsed_json_files/*.json")
    data = []
    for json_file in json_file_names:
        print json_file
        lines = open(json_file, 'r').read().split("\n")
        for line in lines:
            if len(line) == 0:
                continue
            data.append(pd.read_json(line))
    data = pd.concat(data)
    output_data = data
    output_data.to_csv('csv_files/df_text_date.csv', index=False, index_label=True, encoding='utf-8')

    return data


# read json files with python file load
def read_json():
    json_file_names = gb.glob("parsed_json_files/*.json")
    # print json_file_names[0]
    data = []
    for json_file in json_file_names:
        print json_file
        lines = open(json_file, 'r').read().split("\n")
        for line in lines:
            if len(line) == 0:
                continue
            d = json.loads(line)
            # temp_data = pd.read_json(line)
            # temp_data = pd.DataFrame(d.items())
            data.append(d)
    # data = pd.concat(data)
    return data


if __name__ == "__main__":
    tweet_df = pandas_json()
    # print tweet_df.iloc[1]['hash_tags'][0]
    print "Finished reading the json files folder."
