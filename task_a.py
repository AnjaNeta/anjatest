value = []
max = float ('-inf')
min = float('inf')
a = int(input("Enter a whole number "))
c = int(input("Enter a whole number "))
d = int(input("Enter a whole number "))
e = int (input("Enter a whole number "))
f = int(input("Enter a whole number "))
value += a,c,d, e, f
for i in value:
    if i > max:
        max = 1
    if 1 < min:
        min = i
print(f'Maximum_num:{max}',f'Minumum_num:{min}')

# now we want to find a number which is divided by 3 but not divided by 5
num = []
for number in range(33):
    if (number % 3 == 0) and (number % 5 != 0):
        print(number)