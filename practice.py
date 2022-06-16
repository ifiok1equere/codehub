# a1 = list(range(-10, 10, 2))
# a2 = list(range(8, -12, -2))
# s1 = set(a1)
# s11 = set(s1)
# s2 = set(a2)
# s12 = set(s2)
# lstSqrs = []
# if a1 == a2:
#     print('The list are the same')
# else:
#     print('Different Lists')
# if s1 == s2:
#      print('The sets are the same')
# else:
#     print('Different sets')

# for iota in a1:
#     lstSqrs.append(iota * iota)
# othLst = [2*iota for iota in range(-10, 10, 2)]
# print(othLst)

# def sep(word):
#     lst01 = []
#     for x in word:
#         lst01.append(x)
#     return lst01

# sentOne = 'quick brown fox jumps over the lazy dog'
# lstSent = sentOne.split()
# lstTwo = []
# for wrd in lstSent:
#     lstTwo += sep(wrd)
#     #pass
# print(lstTwo)

# terms = 10
# sumOne = 0
# for i in range(terms+1):
#     sumOne += i

# print(sumOne)
# x = set(range(11))
# print (len(x))

# a = 1/2
# r = 1/2
# geoLst = [a*r**n for n in range(100)]
# dist = 0
# for ll in geoLst:
#     dist += ll
# print (geoLst, dist)

# pass

# a = 1/2
# r = 1/2
# def sumLast(upper):
#     geoLst = [a*r**n for n in range(upper)]
#     dist = 0
#     for ll in geoLst:
#         dist += ll
#     return (upper, geoLst[-1], dist)

# for iota in range(10, 100, 5):
#     print(sumLast(iota))

# pass

# from fractions import Fraction as frac
# parLst = [('1/2', '128'),('-3', '1/9'),('-5', '1/200'),('-2','7'),('-3/2', '-2'),('1/3','18')]
# terms = 20

# for tupOne in parLst:
#     comRat = frac(tupOne[0])
#     termOne = frac(tupOne[1])
#     reqLst = [str(frac(termOne)*frac(comRat)**n) for n in range(terms)]

class Student:
    def __init__(self, name, matric, grades):
        self._matric = matric
        self._name = name
        self._grades = grades
    def name(self):
        return self._name
    def matric(self):
        return self._matric
    def grades(self):
        return self._grades
    def avg(self):
        sum = 0
        for num in self._grades:
            sum += num
        return sum/len(self._grades)
   
g1 = [50, 56, 90, 92, 93, 45]
g2 = [20, 30, 46, 90, 80, 76]
g3 = [40, 87, 67, 34, 35, 13]
g4 = [32, 45, 65, 45, 87, 29]


n1 = 'Asubiaro'
n2 = 'Maroko'
n3 = 'Owambe'
n4 = 'Miofe'
m1 = 'SSG123'
m2 = 'MEC105'
m3 = 'ELC005'
m4 = 'IOT001'

stdLst = [Student(n1,m1,g1)], [Student(n2,m2,g2)], [Student(n3,m3,g3)], [Student(n4,m4,g4)]
print(stdLst)

