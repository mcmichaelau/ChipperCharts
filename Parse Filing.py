from sec_api import XbrlApi

xbrlApi = XbrlApi("14273d69ce1d514779e576b1b0188e7c76994483c5e1bab82617dc23169c2870")

#
# "https://www.sec.gov/Archives/edgar/data/1318605/000095017021000046/tsla-20210331.htm"
# "https://www.sec.gov/Archives/edgar/data/1318605/000095017021000524/tsla-20210630.htm"
# "https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000156459020019931/tsla-10q_20200331.htm"

# 10-K HTM File URL example
xbrl_json = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/Archives/edgar/data/320193/000032019322000070/aapl-20220625.htm"
)

# RevenueFromContractWithCustomerExcludingAssessedTax

sections = ['StatementsOfIncome',
'StatementsOfIncomeParenthetical',
'StatementsOfComprehensiveIncome',
'StatementsOfComprehensiveIncomeParenthetical',
'BalanceSheets',
'BalanceSheetsParenthetical',
'StatementsOfCashFlows',
'StatementsOfCashFlowsParenthetical',
'StatementsOfShareholdersEquity',
'StatementsOfShareholdersEquityParenthetical']


for section in sections:

    try:
        print(f'{section}: {xbrl_json[section]}')

    except:
        print('didnt work')