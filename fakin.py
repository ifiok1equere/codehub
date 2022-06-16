ade = {'boxers', 'headphones','slippers',
        'shorts','singlet','wristwatch','teeshirt'}

food = {'pounded yam','boli','rice','dodo','yams',
        'eggs','beans','water melon','mango','egusi',
        'bananas','pine apples','apples', 'eggs','oranges'}

myGarden = {'pawpaw','tomatoes','lemons',
            'bitterleaf','plantains','bananas'}

myToilet = {'watercloset','handsanitizer','wastebin',
            'handwash','washinghandbasin','toiletpaper'}

myKit = {'gascooker','blender','sink','kettle',
            'deepfreezer','pots','pans','mortar',
            'pestle','microwave'}

livRoom = {'wallclock','rug','slidetable'
            'woodsofas','airconditioner','paintings'
            'pottedplants','ceilingfan'}

nigFoot = {'Best Ogedegbe','Rashidi Yekini','Alex Iwobi',
        'Nwankwo Kanu','JJ Okocha','John Mikel Obi',
        'Victor Moses','Odion Ighalo','Ahmed Musa',
        'Obafemi Martins','Segun Ogegbami'}


vehicles = {'bicycle','taxi','car'
            'bolekaja','brt','molue'}

roygbiv = {'red','orange','yellow'
            'green','blue','indigo','violet'}




a = 'Adams Oshiomle'
answer = a in nigFoot
print(answer)


posInt = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,}
numArab = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
if 12 in posInt:
    print('12 is an element of the itersection of posInt and numArab')
else:
    print('12 is not an element of the intersection of posInt and numArab')



posInt = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,}
numArab = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
intSet = numArab.intersection(posInt)
if 12 in intSet:
    print('12 is an element of the itersection of posInt and numArab')
else:
    print('12 is not an element of the intersection of posInt and numArab')

alphaLow = {'a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z'}

alphaUp = {'A','B','C','D','E','F','G','H','I',
            'J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z'}

alphaEng = alphaLow.union(alphaUp)
alphaNumEng = alphaEng.union(numArab)
truFal = True
for elem in posInt:
    if elem in alphaNumEng:
        truFal = True
    else:
        truFal = False
        break
if truFal:
    print('posInt is a subset of alphaNum')
else:
    print('It is not a subset')

tobi = {'boxers','headphones'}

if ade.intersection(tobi) == tobi:
    print("What tobi is wearing is a subset of Ade's ")
else:
    print('There are some things unique to both')

tobi2 ={'boxers','headphones','tennis shoes'}
print('ade union tobi is: ', ade.union(tobi2))
print('tobi union ade is: ', tobi2.union(ade))

authorsLib = {'Faguwa', 'Achebe', 'Shakespeare', 'Milton'
            'Dante', 'Adichie', 'Soyinka', 'Clark', 'Saro Wiwa',
            'Ngugi', 'Nwankwo', 'Austen', 'Eliot', 'Hardy',
            'Bunyan','Tutuola','Delano', 'Ulasi', 'Odunjo'}

myList = {'Olabode','Yuppie','Adamu','Tho','Adichie',
        'Achebe','Soyinka','Nwankwo','Bronte', 'Rakumi','Yinka','Loto', 'Mu'}

myDict = {}
for auth in myList:
    if auth in authorsLib:
        myDict[auth] = 'Available'
    else:
        myDict[auth] = 'Not Available'
        print('The availability list: ', myDict)
 

olu = {'eba','okro','yam','beans',
        'boli','rice','stew'}
chike = {'ugwu','akpu','yam','beans',
        'agazi','rice','plantains'}

diffOne = chike.difference(olu)
diffTwo = olu.difference(chike)
diff3 = olu.difference(olu)

intOne = olu.intersection(chike)
intTwo = chike.intersection(olu)
int3 = olu.intersection(olu)

union1 = olu.union(chike)
union2 = chike.union(olu)
union3 = chike.union(chike)

test1 = len(diffOne) + len(diffTwo) + len(intOne)== len(union1)
test2 = len(diffOne) + len(diffTwo) + len(intTwo)== len(union2)
print(test1,test2)

def sep(word):
    return [char for char in word]
sentOne = 'the quick brown fox jumps over the lazy dog'
listOne = sentOne.split()
firstList = sep(listOne[0])
firstSet = set(firstList)
for word in listOne[1:]:
    firstSet = set(sep(word)).union(firstSet)

print(len(firstSet))

def sep(word):
    return [char for char in word]
sentOne = 'the quick brown fox jumps over the lazy dog'
listOne1 = sep(sentOne)
firstSet1 = set(listOne1)

print(len(firstSet))