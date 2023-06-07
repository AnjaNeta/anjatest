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

number_1 = int (input('Input a number one '))
number_2 = int (input('Input a number two '))
if number_1 < number_2:
    print ('number_1')
elif number_1 > number_2:
    print ('number_2')
elif number_1 == number_2:
    print ('The numbers are equal')
