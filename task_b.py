"""На входе список из чисел, каждое число повторяется два раза, и только одно число повторяется 1 раз. 
Найти число, которое повторяется один раз"""

my_list = input("Enter a list of numbers with a space between them ").split()
print("A list of numbers: ", my_list)
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print("The duplicated numbers in the list ", duplicates)

unique = []
for item in my_list:
    if my_list.count(item) == 1 and item not in unique:
        unique.append(item)
print("The unique number in the list ", unique)
