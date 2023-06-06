# variable_one = int(input())
# variable_two = int(input())
# result_plus = variable_one + variable_two
# result_minus = variable_one - variable_two
# result_many = variable_one * variable_two
# print(result_plus)
# print(result_minus)
# print(result_many)

"""вывести 2 числа,
сравнить их и вывести на экран сначала меньшее,
затем большее, если они равны, написать, что они равны"""

result = int (input('Input a number '))
if result < 10:
    print ('This number is less than 10')
elif result > 10:
    print ('This number is more than 10')
elif result == 10:
    print ('The numbers are equal')
