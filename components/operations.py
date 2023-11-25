import json
from datetime import datetime
from components import userInputs, yahooAPIrequests

def addStockToDict(stockDict, ticker, purchaseDate, purchasePrice, purchaseQTY):
    if ticker in stockDict:
        stockDict[ticker].append({
            'purchaseDate': purchaseDate,
            'purchasePrice': purchasePrice,
            'purchaseQTY': purchaseQTY
        })
    else:
        stockDict[ticker] = [{
            'purchaseDate': purchaseDate,
            'purchasePrice': purchasePrice,
            'purchaseQTY': purchaseQTY
        }]

def updateJson(stockDict):
    with open('stockDict.json', 'w') as f:
        json.dump(stockDict, f, indent=4)

def addStock(stockDict):
    ticker = userInputs.askStockTicker()
    purchaseDate = userInputs.askDate()
    currentPrice = yahooAPIrequests.getSpecificDayOpenPrice(ticker, purchaseDate)
    purchasePrice = userInputs.askNumber(f'Enter the price (Price at purchase date open: ({round(currentPrice,2)}$)): ')
    purchaseQTY = userInputs.askNumber("Enter the quantity: ")

    addStockToDict(stockDict, ticker, purchaseDate, purchasePrice, purchaseQTY)
    updateJson(stockDict)
    print(f'Added {ticker} to your portfolio.')

def calculateAssetsValue(stockDict):
    totalAssetsValue = 0
    for ticker, purchases in stockDict.items():
        for purchase in purchases:
            purchaseDate = purchase['purchaseDate']
            purchaseQTY = purchase['purchaseQTY']
            currentPrice = yahooAPIrequests.getSpecificDayOpenPrice(ticker, purchaseDate)
            totalAssetsValue += currentPrice * purchaseQTY
    return totalAssetsValue