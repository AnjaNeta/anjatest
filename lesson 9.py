# def calender(year, month,date =''):
#     # in_calen = input("enter the date: ").split()
#     # year,month,date = in_calen
#     print("date is {} {} {}".format(year, month,date))
# calender(3,5,2023)

"""принимает неограниченное кол-во насекомых и выводит на печать """
def insects(*args):
    print(args)
insects("butterfly", "fly", "dragonfly")

