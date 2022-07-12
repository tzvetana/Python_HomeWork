#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#version 1 works only with int type
#num = int(input("Enter a number, please:  "))
#def Sum(x):
#    sum = 0
#    while x>0:    
#        sum+=x%10
#        x//=10
#    return sum 
#print(Sum(num))

#version 2 for float type
num = str(input("Enter a number, please:  "))
def Sum(x):
    sum = 0
    x = x.replace('.','')
    x = x.replace(',','')
    for i in x:
        sum+=int(i)
    return sum

print(Sum(num))