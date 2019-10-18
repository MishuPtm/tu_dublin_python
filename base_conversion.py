"""
Author: Ionut Petrescu
Date: 26.09.2019

Updated to allow user to select origin base and output base
"""
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


# Convert from base 10 to any base, takes base and value as integers
def convert_from_decimal(base, value):
    converted_number = ""
    remainder = 0
    while value > 0:
        remainder = value % base
        value = value // base
        converted_number = DIGITS[remainder] + converted_number
    return converted_number


# Converts to base 10, takes input base as integer and value as string
def convert_to_decimal(base, str_value):
    digits = DIGITS[0:base]  # makes sure only digits in this base are displayed
    converted_number = 0
    try:
        for char in str_value.upper():
            converted_number = (converted_number + digits.index(char)) * base
    except ValueError:
        # If exception is raised it means the str_number is not a valid number in this base
        return -1

    return int(converted_number / base)


# Prompts user for a positive integer, takes optional param min and max values
def prompt_input_number(lower_limit=0, upper_limit=99999999999999999):
    input_int = lower_limit - 1

    while True:
        input_str = input()
        try:
            input_int = int(input_str)
        except ValueError:
            print("Must insert a number")

        if lower_limit <= input_int <= upper_limit:
            return input_int
        else:
            print(f"Insert a number between {lower_limit} and {upper_limit}")


# Prompts user to select a base, optional string param 'to' or 'from'
def select_base(desc=None):
    base_int = -1
    while base_int < 0:
        if desc is not None:
            print(f"Insert a base to convert {desc} in the range of 2 and 16 ")
        base_int = prompt_input_number(2, 16)
    return base_int


def insert_number_in_base(base):
    digits = DIGITS[0:base]  # this makes sure we use only digits in this base
    valid_input = False
    number_str = ""

    while not valid_input:
        number_str = input(f"Insert a number in base {base}: ").upper()
        valid_input = True

        for char in number_str:
            if char not in digits:
                valid_input = False

    return number_str


def convert_from_to(input_base, output_base, input_value):
    if input_base == output_base:
        return input_value

    if not input_base == 10:
        input_value = convert_to_decimal(input_base, input_value)

    return convert_from_decimal(output_base, int(input_value))


# This method is useful to use in Computer Technology class to aid with exercises in base 2
def convert_binary_to_decimal_ui():
    while True:
        value = input("Insert binary number ")
        print(f"{value} is {convert_to_decimal(2, value)}")


# Call this method to prompt user for input
def convert_from_to_ui():
    from_base = select_base("from")
    nb_to_convert = insert_number_in_base(from_base)
    to_base = select_base("to")
    result = convert_from_to(from_base, to_base, nb_to_convert)
    print(f"{nb_to_convert} in base {from_base} is {result} in base {to_base}")


#convert_binary_to_decimal_ui()
convert_from_to_ui()
