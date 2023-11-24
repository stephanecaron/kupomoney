from yahooAPIrequests import getSpecificDayOpenPrice, getStockDividends, getStockSplitMultiplier, validateStock
from components import userInputs, operations
from datetime import date

## user enters 1 stock purchase, price and buy date
## Algorithm calculates total return, dividends, splits, etc.
stockDict = {}

print('------------------KUPOMONEY------------------')
def addStock():
    ticker = userInputs.askStockTicker()
    purchaseDate = userInputs.askDate()
    purchasePrice = userInputs.askNumber("Enter the price: ")
    purchaseQTY = userInputs.askNumber("Enter the quantity: ")

    operations.addStockToDict(stockDict, ticker, purchaseDate, purchasePrice, purchaseQTY)


addStock()
print(stockDict)
addStock()
print(stockDict)