#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"],          ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],   ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"],          ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"],                      ищем: "123", ответ: -1
# список: [],                                              ищем: "123", ответ: -1

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
list4 = ["123", "234", "123", "567"]
list5 = []

def Second_contain(list):
    search_data = input('Enter the search data: ')
    count = 0
    if search_data in list:
        for i in  range(len(list)):
            if list[i] == search_data:
                count+=1
                if count==2:
                    print(f'The position of the second occurrence: {i}')
    else:
        print('No, there is no data you are looking for here')

Second_contain(list1)
Second_contain(list2)
Second_contain(list3)
Second_contain(list4)
Second_contain(list5)