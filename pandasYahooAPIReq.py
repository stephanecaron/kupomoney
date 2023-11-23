from datetime import datetime

def getSpecificDayOpenPrice(ticker,startDate, endDate):
if type(startDate) == str:
    date = datetime.strptime(date, dateFormat).date()
data = pdr.get_data_yahoo(ticker, startDate, endDate)
if not data.iloc[0]['Open']:
    return 'did not find anything?'
return data.iloc[0]['Open']


## use this when you need to make heavy requests