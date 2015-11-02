# *****__author__ = 'Yan'*****


import pandas as pd
import glob as gb


def read_json():
    json_file_names = gb.glob("json_files/*.json")
    # print json_file_names[0]
    data = []
    for json_file in json_file_names:
        lines = open(json_file, 'r').read().split("\n")
        for line in lines:
            if len(line) == 0:
                continue
            data.append(pd.read_json(line))
            # print type(data).__name__
    data = pd.concat(data)
    print len(data)
    print "Read all json files."
    return data


if __name__ == "__main__":
    json_content = read_json()
    print "Finished reading the json files folder."
