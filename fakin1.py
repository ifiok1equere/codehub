def plus(a, b, c = None, d = None):
    if c and d:
        return a + b + c + d
    elif c:
        return a + b + c
    else:
        return a + b
                
      
a = 1
b = 2
c = 5
d = -4
e = plus(a, b)

print(e)