from datetime import datetime, date, timedelta
from yahooAPIrequests import validateStock

def askStockTicker():
    while True:
        ticker = input("Enter the stock ticker: ")
        if ticker == "" or not validateStock(ticker):
            print("You have entered an invalid ticker!")
        else:
            return ticker
        
def askDate():
    try:
        date = input("Enter the date (YYYY-mm-dd): ")
        date = datetime.strptime(date, '%Y-%m-%d')
        return date
    except:
        print("You have entered an invalid date!")
        return askDate()
    
def convertStringToDate(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def askNumber(string):
    try:
        price = float(input(string))
        return price
    except:
        print("You have entered an invalid Value!")
        return askNumber()