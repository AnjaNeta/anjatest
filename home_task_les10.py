class Transformer:
    def __init__(self,roman_number ="XIV"):
        self.roman_number = roman_number
def roman_to_decimal(roman_number):
    sum =0
    tallies = {"I":1, "V": 5, "X":10, "L": 50,"C":100, "D": 500, "M":1000}
    for i in range(len(roman_number)-1):
        left = roman_number[i]
        right = roman_number[i+1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[roman_number[-1]]
    return sum
tal = Transformer(sum)
print(roman_to_decimal("MMMXIV"))

roman_numbers = {"M":1000, "D": 500, "C":100, "L": 50,
                 "X":10, "V": 5, "IV": 4, "I": 1}
def decimal_to_roman(number):
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    return roman
print("3014 =", decimal_to_roman(3014))