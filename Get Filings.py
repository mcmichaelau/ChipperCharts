from sec_api import QueryApi
import json
from datetime import date

today = date.today()

ticker = 'aapl'

queryApi = QueryApi(api_key="85931c7acac0406bf1a84465dce73d958335ca73287d46a1179fe930b39c623d")

query = {
    "query": {
        "query_string": {
            "query": "ticker:"+ticker+" AND formType:\"10-Q\""
        }
    },
    "from": "0",
    "size": "100",
    "sort": [
        {
            "filedAt": {
                "order": "desc"
            }
        }
    ]
}

response = queryApi.get_filings(query)


filings = response['filings']

forms = []
i = 0
for file in filings:
    forms.append(json.dumps(file["linkToFilingDetails"]))
    print(json.dumps(file["linkToFilingDetails"], indent=2))
    i = i + 1
