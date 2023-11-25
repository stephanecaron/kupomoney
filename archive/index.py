from yahooAPIrequests import getSpecificDayOpenPrice, getStockDividends, getStockSplitMultiplier
from datetime import date

print('------------------KUPOMONEY------------------')
stock = input("Please enter the ticker name of the stock you purchased (i.e.: MSFT): ")
stockAmount = input("Please enter how many stocks you bought(Interger): ")
purchaseDate = input("Please input the day you purchased the stock (YYYY-mm-dd format): ")
soldQuestion = input("are you still holding this stock?(Y/N): ")

if soldQuestion == 'N':
    soldDate = input("input the date at which you sold this stock(YYYY-mm-dd): ")
else:
    soldDate = date.today()

print('------------------CALCULATING------------------')
buyPrice = getSpecificDayOpenPrice(stock,purchaseDate)
currentOrSoldPrice = getSpecificDayOpenPrice(stock,soldDate)
splits = getStockSplitMultiplier(stock,purchaseDate,soldDate)
dividends = getStockDividends(stock,purchaseDate,soldDate)
stockAmount = float(stockAmount)

buyPrice = buyPrice*splits
initialValue = buyPrice * stockAmount

print(f"You held {stockAmount} {stock} stocks on {purchaseDate} which were individually worth {round(buyPrice,2)}$.")
print(f'your initial total value was {round(initialValue,2)}$.')

if splits>1:
    print('------------------SPLITS------------------')
    print(f'Your {stockAmount} stock were split {splits} times between {purchaseDate} and {soldDate}.')
    newStockAmount = stockAmount * splits
    print(f'Thus you now hold {newStockAmount} {stock} stocks.')

endvalue = currentOrSoldPrice * newStockAmount
totalDividends = round(dividends,2)*newStockAmount
totalValue = endvalue + totalDividends
if dividends>0:
    print('------------------DIVIDENDS------------------')
    print(f'You received {totalDividends}$ in dividends (overestimated)')

print('------------------SUMMARY------------------')
print(f'Your stock value is now {round(currentOrSoldPrice,2)}, up from {round(buyPrice,2)}. ({round((currentOrSoldPrice-buyPrice)*100/buyPrice,2)} % growth gain (this excludes stock splits))')
print(f'Given that you now own {newStockAmount} {stock} stocks, your current value is now {round(endvalue,2)}$')
print(f'If you add your dividend ({totalDividends}$) to your stock Value ({round(endvalue,2)}$),your Total Value is now {round(totalDividends+endvalue,2)}$')
print(f'giving you a total return of {round((totalDividends+endvalue-initialValue)*100/initialValue,2)}%')