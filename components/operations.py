import json
from datetime import datetime
from components import userInputs, yahooAPIrequests
from forex_python.converter import CurrencyRates


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def addStockToDict(
    stockDict, ticker, purchaseDate, purchasePrice, currency, purchaseQTY
):
    if ticker in stockDict:
        stockDict[ticker].append(
            {
                "purchaseDate": purchaseDate,
                "purchasePrice": purchasePrice,
                "currency": currency,
                "purchaseQTY": purchaseQTY,
            }
        )
    else:
        stockDict[ticker] = [
            {
                "purchaseDate": purchaseDate,
                "purchasePrice": purchasePrice,
                "currency": currency,
                "purchaseQTY": purchaseQTY,
            }
        ]


def updateJson(stockDict):
    with open("stockDict.json", "w") as f:
        json.dump(stockDict, f, indent=4)


def addStock(stockDict):
    ticker = userInputs.askStockTicker()
    purchaseDate = userInputs.askDate()
    priceAndCurrency = yahooAPIrequests.getSpecificDayOpenPrice(ticker, purchaseDate)
    currentPrice = priceAndCurrency[0]
    currency = priceAndCurrency[1]
    purchasePrice = userInputs.askNumber(
        f"Enter the price (Price at purchase date open: ({round(currentPrice,2)}$ {currency})): "
    )
    purchaseQTY = userInputs.askNumber("Enter the quantity: ")

    addStockToDict(
        stockDict, ticker, purchaseDate, purchasePrice, currency, purchaseQTY
    )
    updateJson(stockDict)
    print(f"Added {ticker} to your portfolio.")


def calculateInitialAssetsValue(stockDict):
    totalAssetsValue = 0
    for ticker, purchases in stockDict.items():
        for purchase in purchases:
            purchaseDate = purchase["purchaseDate"]
            purchaseQTY = purchase["purchaseQTY"]
            currentPrice = yahooAPIrequests.getSpecificDayOpenPrice(
                ticker, purchaseDate
            )[0]
            totalAssetsValue += currentPrice * purchaseQTY
    return totalAssetsValue


def getCurrencyConversionForTargetDate(currentCurrency, targetCurrency, targetDate):
    if currentCurrency == targetCurrency:
        return 1
    else:
        return CurrencyRates().get_rate(
            currentCurrency, targetCurrency, date_obj=targetDate
        )


def calculateCurrentAssetsValue(stockDict, userCurrency):
    todayDate = datetime.today().date()
    totalValue = 0
    for ticker, stocks in stockDict.items():
        stockQTYReserve = 0
        for stock in stocks:
            stockQTY = stock["purchaseQTY"]
            stockQTYReserve += stockQTY
        priceAndCurrency = yahooAPIrequests.getSpecificDayOpenPrice(ticker, todayDate)
        currentStockPrice = priceAndCurrency[0]
        stockCurrency = priceAndCurrency[1]
        if userCurrency != stockCurrency:
            currencyConversion = getCurrencyConversionForTargetDate(
                stockCurrency, userCurrency, todayDate
            )
            currentStockPrice = currentStockPrice * currencyConversion
        stockValue = currentStockPrice * stockQTYReserve
        print("------")
        print(
            f"{bcolors.HEADER}{ticker}{bcolors.ENDC} :\n{stockQTY} units at {round(currentStockPrice,2)}$ {userCurrency}\n{bcolors.OKCYAN}{round(stockValue,2)}$ total stock value{bcolors.ENDC}"
        )
        totalValue += stockValue
    print("-----")
    print(
        f"{bcolors.OKGREEN}{round(totalValue, 2)}$ {userCurrency} Total Portfolio Value{bcolors.ENDC}"
    )


def changeUserSettings(userSettings):
    userSettings["currency"] = userInputs.askCurrency(f"Enter your currency: ")
    with open("userSettings.json", "w") as f:
        json.dump(userSettings, f, indent=4)
    print(
        f'{bcolors.OKGREEN}Changed currency to {userSettings["currency"]} {bcolors.ENDC}'
    )
