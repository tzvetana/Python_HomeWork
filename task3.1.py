#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list = ['123', 'dshfohy', '683ww','hslkfl','2937']

def Count_presence(list):
    x = input('Enter the search data: ')
    count = list.count(x)
    if count>0:
        print(f'Yes, {x} is in the list')
    else:
        print(f'No, {x} is not in the list')

Count_presence(my_list)