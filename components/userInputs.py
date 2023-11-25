from datetime import datetime, date, timedelta
from components import operations, yahooAPIrequests

def askStockTicker():
    while True:
        ticker = input("Enter the stock ticker: ")
        if ticker == "" or not yahooAPIrequests.validateStock(ticker):
            print("You have entered an invalid ticker!")
        else:
            return ticker
        
def askDate():
    try:
        date = input("Enter the date (YYYY-mm-dd): ")
        return date
    except:
        print("You have entered an invalid date!")
        return askDate()

def askNumber(string):
    while True:
        try:
            number = float(input(string))
            return number
        except ValueError:
            print("You have entered an invalid Value!")
        except KeyboardInterrupt:
            print("\nYou have cancelled the input!")
            break