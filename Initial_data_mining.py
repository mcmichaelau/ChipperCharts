from sec_api import QueryApi
from sec_api import XbrlApi
import json
from datetime import date
import csv
from functools import reduce


xbrlApi = XbrlApi("5782bc5ddc0174fa94a2b8b714414e595ce803c4b5b46807cfe54c0f360ea407")


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


# method to collect and store keys to wanted values
def collect_keys(ticker, url, values_list):
    ticker_json = xbrlApi.xbrl_to_json(htm_url=url)

    keys_list = []

    for value in values_list:
        print(value)
        keys = find_index(ticker_json, value)
        keys_list.append(keys)

    print(f'keys list: {keys_list}')

    test = []
    test.append(keys_list)

    # save keys list to a file
    with open(f'{ticker}_keys.csv', 'w', newline='') as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the list to the csv
        writer.writerow(keys_list)

    return keys_list


values = ['19532000000','1575000000','2192000000','10327000000','2364000000','35990000000','4824000000','5562000000','21926000000','2251000000','218000000','228000000','191000000','3236000000','74426000000','8880000000','1579000000']

url = 'https://www.sec.gov/Archives/edgar/data/1318605/000095017022019867/tsla-20220930.htm'
test = collect_keys('TSLA', url, values)
