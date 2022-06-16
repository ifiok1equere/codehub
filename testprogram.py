from turtle import clear
a = input('Enter a celcius tempearture value you wish to convert: ')
a = float(a)
b = (a * (9/5)) + 32
b = str(float(b))
print("Your farenheight equivalent temperature is " + b + "F")
