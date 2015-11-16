import json
# from pprint import pprint
import os.path
def parse_json_file(directory, file_name):
    name = os.path.join(directory + file_name + "." + json)
    with open(name) as data_file:
        data = json.load(data_file)

    # pprint(data)