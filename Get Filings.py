from sec_api import QueryApi
import json
from datetime import date

today = date.today()

queryApi = QueryApi(api_key="14273d69ce1d514779e576b1b0188e7c76994483c5e1bab82617dc23169c2870")

query = {
    "query": {
        "query_string": {
            "query": "ticker:AAPL AND formType:\"10-Q\""
        }
    },
    "from": "0",
    "size": "10",
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
