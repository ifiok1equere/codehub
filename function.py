temp = input('enter the celsius temperature you want to convert: ')
# if type(temp) == 'str':
#     print('Your entry is invalid, please enter a number')
#     break
# else:
#     continue

def tempConverter():
    newTemp = (int(temp) - 32) * (5/9)
    print('Your temperature in farenheit is: ', int(newTemp))

tempConverter()



def Userloop():
    data = input('Enter a value you want to loop over: ')
    data2 = len(data) - (len(data)-4)
    data3 = []
    i = 0
    for x in range(data2):
        data3.append(data[i])
        i = i + 1
        if len(data3) == data2:
            print(data3)
        else:
            continue
Userloop()



def marketlist():
    MarketList = []
    while True:
        item = str(input('Enter an item that will make up your list: '))
        if item.lower() == "stop":
            print('Here is your market list: ', MarketList)
            break
        else:
            MarketList.append(item)
marketlist()
