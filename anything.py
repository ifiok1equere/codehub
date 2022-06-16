import portion as interval
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt


intval1 = interval.openclosed(0, 5)
answer = 1.2 in intval1
print(answer)


a = [1, 2, 4, 6, 8, 10]
b = ['ifiok', 'ima', 'nse', 'alfred', 'edidiong', 'rose']
c = dict(zip(b, a))
print(c)
c['ifiok'] = 100
print(c)

myset = set()
print(type(myset))

def run(context):
    try:
        upper = 100
        primeList = []
        for iota in range(upper):
            primeList.append(iota)
        for iota in range(1, upper):
            for jota in range(iota + iota, upper, iota):
                if primeList[iota] == 1:
                    break
                primeList[jota] = 1
        primeSet = set(primeList)
        primeSet.discard(0)
        primeSet.remove(1)
        pass  
    except:
        pass
    
run(1)

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
        
print(find_max([10, -2, 3, -4, 36]))

class Calculator:
    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2      
              
    def addition(self):
        return self.operand_1 + self.operand_2
    
    def subtraction(self):
        return self.operand_1 - self.operand_2

    def multiplication(self):
        return self.operand_1 * self.operand_2

    def division(self):
        return self.operand_1 / self.operand_2
    
    def exponential(self):
        return self.operand_1 ** self.operand_2
    
    def choice(self, user_choice):
        if user_choice == "'+":
            return self.addition
        elif user_choice == '-':
            return self.subtraction
        elif user_choice == '*':
            return self.multiplication
        elif user_choice == '/':
            return self.division
        elif user_choice == '**':
            return self.exponential
       
    
solution = Calculator(4, 5, 6)
print(solution.exponential)