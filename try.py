# input('enter a number as x ').split()
degree = input().split()
temp = input().split()
def func(degree, temp):
    if temp == "fahrenheit":
        degree = (degree * 1.8) +32
    elif temp == "celcius":
        degree = (degree -32) /1.8
    return degree
print(func(degree,temp))
