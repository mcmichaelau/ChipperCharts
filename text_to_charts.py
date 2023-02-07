import pandas as pd
import csv
from sec_api import QueryApi
from sec_api import XbrlApi
import json
from datetime import date
import csv
from functools import reduce
import ast

form_url = 'https://www.sec.gov/Archives/edgar/data/1318605/000095017021002253/tsla-20210930.htm'

xbrlApi = XbrlApi("85931c7acac0406bf1a84465dce73d958335ca73287d46a1179fe930b39c623d")

json_data = xbrlApi.xbrl_to_json(htm_url=form_url)


# method to find the index of a value
def find_index(obj, value):
    """
    Find the index of a value within a nested dictionary or list
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v == value:
                return [k]
            elif isinstance(v, (dict, list)):
                index = find_index(v, value)
                if index is not None:
                    return [k] + index
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if v == value:
                return [i]
            elif isinstance(v, (dict, list)):
                index = find_index(v, value)
                if index is not None:
                    return [i] + index
    return None

# open text file
with open('test.txt', 'r') as f:
    # read the file
    data = f.read()
    # split the file into a list
    data = data.splitlines()

    # split each item in the list by spaces
    for i in range(len(data)):
        data[i] = data[i].split(' ')


# this converts the list of values to a list of indices
chart_keys = []
# loop through the list
for i in range(1, len(data)):
    # create new item in the list
    chart_keys.append([])
    # loop through each item in the list
    for j in range(len(data[i])):
        # remove commas from each item
        data[i][j] = data[i][j].replace(',', '')
        # multiply each item by 1000000
        data[i][j] = str(int(data[i][j]) * 1000000)
        # find the index of the item that contains the value
        print(data[i][j])
        index = find_index(json_data, data[i][j])
        # add the index to the list
        chart_keys[i-1].append(index)

print(chart_keys)
