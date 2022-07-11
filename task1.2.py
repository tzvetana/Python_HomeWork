#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

num1 = int(input('Enter the X-axis coordinate:  '))
num2 = int(input('Enter the Y-axis coordinate:  '))

def Quarter(x,y):
    if x>0 and y>0:
        print("You're in the first quarter")
    elif x<0 and y>0:
        print("You're in the second quarter")
    elif x<0 and y<0:
        print("You're in the third quarter")
    elif x>0 and y<0:
        print("You're in the fourth quarter")
    elif x == 0:
        print("Your point is on the Y-axis")
    elif y ==0:    
        print("Your point is on the X-axis")
    else:
        print("You're standing at the starting point. Where are we going?")

Quarter(num1,num2)