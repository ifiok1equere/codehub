#Question 1:
''' Make the while loop spell out ifiok as a single letter a = "Ifiok" '''

#1st Method
b = 'Ifiok'
i = 0
while i in range(len(b)):
    print(b[i])
    i = i + 1
    
#2nd Method
b = 'Ifiok'
i = 0
while i < len(b):
    print(b[i])
    i = i + 1

#Question 2: 
''' Write an app that allows a user to write down
market items and the user should enter 'stop' to stop the app. 
When the app is stopped, the app should output the list of market items '''

#CONDITION: When user isnt sure about how many items will make up the market list:
MarketList = []
while True:
    item = str(input('Enter an item that will make up your list: '))
    if item.lower() == "stop":
        break
    else:
        MarketList.append(item)
print('Here is your market list: ', MarketList)

#For_loop
a = 'ifiok'
for x in a:
    print(x)

#CODINTION 1: When user has a definite number of list in mind:

item1 = int(input('How many items do you want in your market list? '))
i = 0
MarketList = []
while i in range(0,item1):
    item2 = str(input('Enter an item that will make up your list: '))
    MarketList.append(item2)
    decide = input('Enter "continue" to add another item or enter "stop" to finish your list: ')
    
    if decide.lower() == 'stop':
        break
    else:
        continue
    i = i + 1

print('Here is your market list: ', MarketList)
