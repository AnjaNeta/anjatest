# def calender(year, month,date =''):
#     # in_calen = input("enter the date: ").split()
#     # year,month,date = in_calen
#     print("date is {} {} {}".format(year, month,date))
# calender(3,5,2023)

# """принимает неограниченное кол-во насекомых и выводит на печать """
# def insects(*args):
#     print(args)
# insects("butterfly", "fly", "dragonfly")

"""принимает марка автомобиля и его модель, которая по умолчанию"""
from typing import List, Any

# def salon(car_brand,model ='q7'):
#     print("{} {}".format(car_brand,model))
# salon("hyundai")

"""функция ничего не принимает на вход, внутри содержится фраза : "привет, питонист" 
и функцию, которая выводит на печать"""

# def func():
#     hi = "hello, pythonist!"
#     def phrase():
#         print(hi)
#     phrase()
# func()

"""подсчет согласных и гласных в английском языке и вывод их"""
word = input("Spring day")
consonant =[]
vocal =[]
count =0
all_vocals = ["a", "e", "i", "o","u", "y"]
def english():
    for i in word:
        if i in all_vocals:
        count +=1
    else:
    consonant +=1
print("the count of vocals ",vocal)
print("the count of consonants ", consonant)

english(word)