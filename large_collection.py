import pandas as pd
import csv
from sec_api import QueryApi
from sec_api import XbrlApi
import json
from datetime import date
import csv
from functools import reduce
import ast


xbrlApi = XbrlApi("5782bc5ddc0174fa94a2b8b714414e595ce803c4b5b46807cfe54c0f360ea407")

url_list = [
            # "https://www.sec.gov/Archives/edgar/data/1318605/000095017022012936/tsla-20220630.htm",
            "https://www.sec.gov/Archives/edgar/data/1318605/000095017022006034/tsla-20220331.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000095017021002253/tsla-20210930.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000095017021000524/tsla-20210630.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000095017021000046/tsla-20210331.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459020047486/tsla-10q_20200930.htm"
            # "https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000156459020033670/tsla-10q_20200630.htm"
            # "https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000156459020019931/tsla-10q_20200331.htm"
            # "https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000156459019038256/tsla-10q_20190930.htm"
            # "https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000156459019026445/tsla-10q_20190630.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459019013462/tsla-10q_20190331.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459018026353/tsla-10q_20180930.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459018019254/tsla-10q_20180630.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459018011086/tsla-10q_20180331.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459017021343/tsla-10q_20170930.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459017015705/tsla-10q_20170630.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459017009968/tsla-10q_20170331.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459016026820/tsla-10q_20160930.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459016023024/tsla-10q_20160630.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459016018886/tsla-10q_20160331.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459015009741/tsla-10q_20150930.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459015006666/tsla-10q_20150630.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000156459015003789/tsla-10q_20150331.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312514403635/d812482d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312514303175/d766922d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312514192606/d715897d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312513435480/d588506d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312513327916/d549636d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312513212354/d511008d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312512457610/d410318d10q.htm"
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312512332138/d364775d10q.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312512225825/d325967d10q.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312511308489/d226201d10q.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312511221497/d10q.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312511139677/d10q.htm",
            # "https://www.sec.gov/Archives/edgar/data/1318605/000119312510259068/d10q.htm",
]

url = 'https://www.sec.gov/Archives/edgar/data/1318605/000095017022019867/tsla-20220930.htm'
#
# json_data = xbrlApi.xbrl_to_json(htm_url=url)

working_list = []

# read each row of local csv
with open('TSLA_keys.csv', 'r') as f:
    reader = csv.reader(f)
    # read all rows
    keys_list = list(reader)

    for key in keys_list[0]:
        key = ast.literal_eval(key)
        working_list.append(key)

# iterate through each url in url list
for url in url_list:
    # get json data
    print('----------------------------------------')
    json_data = xbrlApi.xbrl_to_json(htm_url=url)
    for key in working_list:

        try:
            # use key to find value
            result = reduce(lambda d, k: d[k], key, json_data)

            print(result)

        except:
            print('Key not found: ', key)







