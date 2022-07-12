#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

limit = int(input("Enter a number, please:  "))

def Multiplicate(x):
    mult = 1
    mult_list = []
    for i in range(1,x+1):
            mult*=i
            mult_list.append(mult)
    print("There is a set of multiplication numbers from 1 to the limit")
    print(mult_list)

Multiplicate(limit)

        
