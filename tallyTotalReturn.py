from components import userInputs, operations
from datetime import date
import json

## user enters 1 stock purchase, price and buy date
## Algorithm calculates total return, dividends, splits, etc.
userSettings = json.load(open('userSettings.json'))
currency = userSettings['currency']
stockDict = json.load(open('stockDict.json'))

while True:
    print('------------------MENU------------------')
    print('1. Add Stock')
    print('2. Calculate Total Return')
    print('3. Calculate current Value')
    print('4. Change User Settings (Display Currency)')
    print('5. Exit')
    print('----------------------------------------')
    choice = userInputs.askNumber('Enter your choice: ')

    if choice == 1:
        operations.addStock(stockDict)
        stockDict = json.load(open('stockDict.json'))
    elif choice == 2:
        print('Not implemented yet')
    elif choice == 3:
        print('----------------------------------------')
        print('calculating...')
        print(f'hey big boy you\'re currently worth {round(operations.calculateCurrentAssetsValue(stockDict, currency),2) }$ {currency}')
        print('----------------------------------------')
        print(f'individual value to be implemented')
    elif choice == 4:
        operations.changeUserSettings(userSettings)
        userSettings = json.load(open('userSettings.json'))
        currency = userSettings['currency']
    elif choice == 5:
        break