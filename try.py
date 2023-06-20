# input('enter a number as x ').split()
# degree = int(input())
# temp = str(input())
# def func(degree, temp):
#     if temp == "fahrenheit":
#         degree = (degree * 1.8) +32
#     elif temp == "celcius":
#         degree = (degree -32) /1.8
#     return degree
# print(func(degree,temp))


# задача про високосный год
def year_func(time):
    if time % 4 ==0 and time % 100 != 0 or time % 400 == 0:
        return "YES"
    else:
        return "NO"
print(year_func(1600))
