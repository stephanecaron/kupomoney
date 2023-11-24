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


##duno whats happening below here this bad boy just doing shit lmao
def calculateTotalReturn(stockDict):
    totalReturn = 0
    for ticker in stockDict:
        for purchase in stockDict[ticker]:
            purchaseDate = purchase['purchaseDate']
            purchasePrice = purchase['purchasePrice']
            purchaseQTY = purchase['purchaseQTY']
            soldDate = date.today()
            soldPrice = getSpecificDayOpenPrice(ticker, soldDate)
            splits = getStockSplitMultiplier(ticker, purchaseDate, soldDate)
            dividends = getStockDividends(ticker, purchaseDate, soldDate)
            totalReturn += calculateTotalReturnForStock(purchaseDate, purchasePrice, purchaseQTY, soldDate, soldPrice, splits, dividends)
    return totalReturn

def calculateTotalReturnForStock(purchaseDate, purchasePrice, purchaseQTY, soldDate, soldPrice, splits, dividends):
    initialValue = purchasePrice * purchaseQTY
    endvalue = soldPrice * purchaseQTY * splits
    totalDividends = dividends * purchaseQTY
    totalValue = endvalue + totalDividends
    return totalValue - initialValue