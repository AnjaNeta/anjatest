"""На входе список чисел, требуется вывести максимальное и минимальное
и все числа, которые делятся на три, но не делятся на пять"""
num = list()
for number in range(3,33,3):
    if (number % 3 ==0) and (number % 5!=0):
        print(number)
    num.append(number)
print('A list of numbers:', num)
print('max: ', max(num))
print('min=: ', min(num))
