#1 Qustion 1
class Car:
    def __init__(self, color, milleage):
        self.color = color
        self.milleage = milleage

benz = Car('blue', 20000)
lexus = Car('red', 30000)

print(benz.color, benz.milleage)
print(lexus.color, lexus.milleage)

# Question 2
class Citizen:
    def __init__(self, name, age, state, bvn, phone):
        self.name = name
        self.age = age
        self.state = state
        self.bvn = bvn
        self.phone = phone

first_citizen = Citizen('keziah', 26, 'akwa-ibom', 2014510202, '08100000025')
second_citizen = Citizen('alfred', 70, 'abia', 2025774120, '08170000031')
third_citizen = Citizen('david', 39, 'lagos', 2210562310, '08130000046')
fourth_citizen = Citizen('mohammed', 18, 'kaduna', 2014510202, '08100300079')

print(first_citizen.name, first_citizen.age, first_citizen.state, first_citizen.bvn, first_citizen.phone)
print(second_citizen.name, second_citizen.age, second_citizen.state, second_citizen.bvn, second_citizen.phone)
print(third_citizen.name, third_citizen.age, third_citizen.state, third_citizen.bvn, third_citizen.phone)
print(fourth_citizen.name, fourth_citizen.age, fourth_citizen.state, fourth_citizen.bvn, fourth_citizen.phone)