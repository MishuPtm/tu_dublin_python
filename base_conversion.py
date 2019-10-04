"""
Author: Ionut Petrescu
Date: 26.09.2019
Converting from base 10 to any base between 2 and 16
"""


def convert_from_decimal(base, number):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    converted_number = ""
    remainder = 0
    while number > 0:
        remainder = number % base
        number = number // base
        converted_number = digits[remainder] + converted_number
    return converted_number


def convert_to_decimal(base, str_number):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    digits = digits[0:base]     # makes sure only digits in this base are displayed
    converted_number = 0
    try:
        for char in str_number.upper():
            converted_number = (converted_number + digits.index(char)) * base
    except ValueError:
        # If exception is raised it means the str_number is not a valid number in this base
        return -1

    return int(converted_number / base)


def prompt_input_number(lower_limit=0, upper_limit=99999999999999999):
    input_str = input()
    input_int = -1
    try:
        input_int = int(input_str)
    except ValueError:
        print("Must insert a number")
        return -1
    if lower_limit <= input_int <= upper_limit:
        return input_int
    else:
        print(f"Insert a number between {lower_limit} and {upper_limit}")
        return -2


def convert_to_decimal_ui():
    base_int = -1
    print("Converting to decimal")
    while base_int < 0:
        print("Insert a base from 2 to 16\n")
        base_int = prompt_input_number(2, 16)
    number_str = input(f"Insert a number in base {base_int}: ")
    result = convert_to_decimal(base_int, number_str)
    if result == -1:
        print(f"{number_str} is not a valid number in base {str(base_int)}")
    else:
        print(f"{number_str} in base {base_int} is {result} in decimal")


def convert_from_decimal_ui():
    print("Converting from decimal")
    base_int = -1
    number_int = -1
    while base_int < 0:
        print("Insert a base from 2 to 16\n")
        base_int = prompt_input_number(1, 17)
    while number_int < 0:
        print(f"Insert a positive number to convert to base {base_int} \n")
        number_int = prompt_input_number()

    print(f"{number_int} in base {base_int} is {convert_from_decimal(base_int, number_int)}")


bin = "1001010101110"
#print(convert_to_decimal(2, bin))
convert_from_decimal_ui()