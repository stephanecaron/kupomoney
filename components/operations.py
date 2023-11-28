import json
from datetime import datetime
from components import userInputs, yahooAPIrequests
from forex_python.converter import CurrencyRates

def addStockToDict(stockDict, ticker, purchaseDate, purchasePrice,currency, purchaseQTY):
    if ticker in stockDict:
        stockDict[ticker].append({
            'purchaseDate': purchaseDate,
            'purchasePrice': purchasePrice,
            'currency': currency,
            'purchaseQTY': purchaseQTY
        })
    else:
        stockDict[ticker] = [{
            'purchaseDate': purchaseDate,
            'purchasePrice': purchasePrice,
            'currency': currency,
            'purchaseQTY': purchaseQTY
        }]

def updateJson(stockDict):
    with open('stockDict.json', 'w') as f:
        json.dump(stockDict, f, indent=4)

def addStock(stockDict):
    ticker = userInputs.askStockTicker()
    purchaseDate = userInputs.askDate()
    priceAndCurrency = yahooAPIrequests.getSpecificDayOpenPrice(ticker, purchaseDate)
    currentPrice = priceAndCurrency[0]
    currency = priceAndCurrency[1]
    purchasePrice = userInputs.askNumber(f'Enter the price (Price at purchase date open: ({round(currentPrice,2)}$ {currency})): ')
    purchaseQTY = userInputs.askNumber("Enter the quantity: ")

    addStockToDict(stockDict, ticker, purchaseDate, purchasePrice, currency, purchaseQTY)
    updateJson(stockDict)
    print(f'Added {ticker} to your portfolio.')

def calculateInitialAssetsValue(stockDict):
    totalAssetsValue = 0
    for ticker, purchases in stockDict.items():
        for purchase in purchases:
            purchaseDate = purchase['purchaseDate']
            purchaseQTY = purchase['purchaseQTY']
            currentPrice = yahooAPIrequests.getSpecificDayOpenPrice(ticker, purchaseDate)[0]
            totalAssetsValue += currentPrice * purchaseQTY
    return totalAssetsValue

def getCurrencyConversionForTargetDate(currentCurrency, targetCurrency, targetDate):
    if currentCurrency == targetCurrency:
        return 1
    else:
        return CurrencyRates().get_rate(currentCurrency,targetCurrency, date_obj=targetDate)


def calculateCurrentAssetsValue(stockDict, userCurrency):
    totalAssetsValue = 0
    todayDate = datetime.today().date()
    for ticker, stocks in stockDict.items():
        for stock in stocks:
            stockQTY = stock['purchaseQTY']
            stockCurrency = stock['currency']
            currentPrice = yahooAPIrequests.getSpecificDayOpenPrice(ticker, todayDate)[0]
            if userCurrency != stockCurrency:
                currencyConversion = getCurrencyConversionForTargetDate(stockCurrency, userCurrency, todayDate)
                currentPrice = currentPrice * currencyConversion
            totalAssetsValue += currentPrice * stockQTY
    return totalAssetsValue

def changeUserSettings(userSettings):
    userSettings['currency'] = userInputs.askCurrency(f'Enter your currency: ')
    with open('userSettings.json', 'w') as f:
        json.dump(userSettings, f, indent=4)
    print(f'Changed currency to {userSettings["currency"]}')