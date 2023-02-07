from sec_api import QueryApi
from sec_api import XbrlApi

xbrlApi = XbrlApi("85931c7acac0406bf1a84465dce73d958335ca73287d46a1179fe930b39c623d")

url = 'https://www.sec.gov/Archives/edgar/data/320193/000032019322000070/aapl-20220625.htm'

ticker_json = xbrlApi.xbrl_to_json(htm_url=url)

# print((ticker_json['StatementsOfIncome']['OperatingExpenses']))


def find_final_values(d):
    result = []
    for key, value in d.items():
        if isinstance(value, dict):
            result.extend(find_final_values(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, (dict, list)):
                    result.extend(find_final_values(item))
                else:
                    if key == 'value':
                        result.append(item)
        else:
            if key == 'value':
                result.append(value)
    return result

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


values = find_final_values(ticker_json)
#
print(values)

# test = find_index(ticker_json, '696969')

# print(test)


# print(ticker_json.keys())
