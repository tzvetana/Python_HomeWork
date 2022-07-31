#Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
#Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом 
# и вывести получившуюся статистику.
#Программа должна считывать одну строку со стандартного ввода 
# и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
# в формате "слово количество" (см. пример вывода).Порядок вывода слов может быть произвольным, 
# каждое уникальное слово﻿ должно выводиться только один раз.
# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

from dataclasses import replace

text = input("Enter the text: ")

def count_words(text):
    text = text.lower()
    words = text.split()
    words.sort()
    
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word]+1
        else:
             words_dict[word] = 1

    print(f"The number of words: {len(words)}")
    print(f"The number of unique words: {len(words_dict)}")
    
    for key,value in words_dict.items(): 
        print(key, ':', value)


count_words(text)
