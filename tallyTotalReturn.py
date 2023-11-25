from components import userInputs, operations
from datetime import date
import json

## user enters 1 stock purchase, price and buy date
## Algorithm calculates total return, dividends, splits, etc.
stockDict = json.load(open('stockDict.json'))
print('---------------KUPOMONEY---------------')
print(f' hey big boy you\'re currently worth {round(operations.calculateAssetsValue(stockDict),2)}$')

while True:
    print('------------------MENU------------------')
    print('1. Add Stock')
    print('2. Calculate Total Return')
    print('3. Exit')
    choice = userInputs.askNumber('Enter your choice: ')

    if choice == 1:
        operations.addStock(stockDict)
    elif choice == 2:
        print('Not implemented yet')
    elif choice == 3:
        break