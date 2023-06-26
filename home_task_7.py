"""1.программа, принимающая на вход слова через запятую и выводящая слова в алфавитном порядке"""
# text = input("Enter some words: ")
# def favbook(text):
#     book_list =[i for i in text.split()]
#     book_list.sort()
#     return print(book_list)
# favbook(text)

"""2.написать программу, которая принимает на вход список (1,2,3) и выводит все возможные комбинации его членов
по типу (1,2,3),(1,3,2)"""
# import itertools
# digits = [1,2,3]
# # print(list(itertools.combinations_with_replacement(digits,3)))
# products=list(itertools.product(digits, repeat =3))
# print(products)

'''3.функция permutation in itertools, вывести все возможные варианты из списка (1,2,3)'''
# import itertools
# digits = [1,2,3]
# permutations = list(itertools.permutations(digits))
# print(permutations)

"""4.использовать random.sample и сгенерировать список случайных чисел, используя лист компрехеншн"""
"""первый способ"""
# from random import randint
# lst = [randint(-100, 100) for i in range(10)]
# print(lst)
"""второй способ"""
# import random
# list = [100, 200, 13, 7, 11, 45, 22, 34, 125, 78, 0]
# print(random.sample(list, 3))

"""5. написать функцию, которая принимает на вход неограниченное кол-во аргументов, а на выходе возвращает их сумму
использовать args"""

"""args со звездочкой нужен, когда хотим передать неизвестное кол-во аргументов"""
def sum_all(*args):
    try:
        return sum(int(i) for i in args)
    except:
        return False
print(sum_all(1,2,3,4,5))