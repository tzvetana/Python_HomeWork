#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

daynum = int(input('Enter the day number, please:  '))

def Weekend(x1):
    if 0<x1<6:
        print("No, go to work again")
    elif x1 == 6 or x1 == 7:
        print("Yes! It's the day of freedom from worries")
    else:
        print("Dude , you 've been working hard ! There are only 7 days in a week!!!")

Weekend(daynum)