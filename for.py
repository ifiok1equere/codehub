a = 'ifiok'
for b in a:
    print(b)

#List Maker
MarketList = []
data = input('How many items do you want to make your list?: ')
data = int(data)
for list in range(data):
    item = str(input('Enter an item that will make up your list: '))
    if item.lower() == "stop":
        break
    elif item.lower() == '':
        print('Sorry, you have not entered any item to your list. Try again.')
    else:
        MarketList.append(item)
print('Here is your market list: ', MarketList)

