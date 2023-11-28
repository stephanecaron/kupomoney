from datetime import datetime, date, timedelta
from components import operations
import yfinance as yf


def convertStringToDate(date):
    return datetime.strptime(date, "%Y-%m-%d").date()


def getSpecificDayOpenPrice(ticker, targetDate):
    if type(targetDate) == str:
        targetDate = convertStringToDate(targetDate)
    ticker = yf.Ticker(ticker)
    data = ticker.history(
        start=targetDate, end=targetDate + timedelta(days=3)
    )  # theres no specific date API request, if start = end, you get nothing
    if not data.iloc[0]["Open"]:
        return 0
    return [float(data.iloc[0]["Open"]), (ticker.info["currency"])]


def getStockSplitMultiplier(ticker, startDate, endDate):
    if endDate is None:
        endDate = datetime.today().date()
    else:
        endDate = convertStringToDate(endDate)
    startDate = convertStringToDate(startDate)
    ticker = yf.Ticker(ticker)
    splits = ticker.splits
    totalSplits = 0
    for date, split in splits.items():
        if startDate <= date.date() <= endDate:
            totalSplits += split
    return float(totalSplits)


def getStockDividends(ticker, startDate, endDate):
    if endDate is None:
        endDate = datetime.today().date()
    elif type(endDate) == str:
        endDate = convertStringToDate(endDate)
    startDate = convertStringToDate(startDate)
    ticker = yf.Ticker(ticker)
    dividends = ticker.dividends
    totalDividends = 0
    for date, dividend in dividends.items():
        if startDate <= date.date() <= endDate:
            totalDividends += dividend
    return float(totalDividends)


def validateStock(ticker):
    ticker = yf.Ticker(ticker)
    try:
        ticker.info
        return True
    except:
        return False
