from datetime import datetime, date, timedelta
from components import operations, yahooAPIrequests
import yfinance as yf
import json

ticker = "VFV.TO"
targetDate = "2023-11-28"


def getFullInfo(ticker, targetDate):
    if type(targetDate) == str:
        targetDate = yahooAPIrequests.convertStringToDate(targetDate)
    ticker = yf.Ticker(ticker)
    return ticker


def getPrice(ticker, targetDate):
    if type(targetDate) == str:
        targetDate = yahooAPIrequests.convertStringToDate(targetDate)
    ticker = yf.Ticker(ticker)
    data = ticker.history(
        start=targetDate, end=targetDate + timedelta(days=3)
    )  # theres no specific date API request, if start = end, you get nothing
    if not data.iloc[0]["Open"]:
        return 0
    return float(data.iloc[0]["Open"])


print(getPrice(ticker, targetDate))
print(getFullInfo(ticker, targetDate).info["currency"])
