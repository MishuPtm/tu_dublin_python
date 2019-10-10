"""
Author: Ionut Petrescu
Date: 26.09.2019
Converting from base 10 to any base between 2 and 16
"""
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def convert_from_decimal(base, number):
    converted_number = ""
    remainder = 0
    while number > 0:
        remainder = number % base
        number = number // base
        converted_number = DIGITS[remainder] + converted_number
    return converted_number


def convert_to_decimal(base, str_number):
    digits = DIGITS[0:base]  # makes sure only digits in this base are displayed
    converted_number = 0
    try:
        for char in str_number.upper():
            converted_number = (converted_number + digits.index(char)) * base
    except ValueError:
        # If exception is raised it means the str_number is not a valid number in this base
        return -1

    return int(converted_number / base)


def prompt_input_number(lower_limit=0, upper_limit=99999999999999999):
    input_int = lower_limit - 1

    while input_int < lower_limit:
        input_str = input()
        try:
            input_int = int(input_str)
        except ValueError:
            print("Must insert a number")

        if lower_limit <= input_int <= upper_limit:
            return input_int
        else:
            print(f"Insert a number between {lower_limit} and {upper_limit}")


def select_base(desc):
    base_int = -1
    while base_int < 0:
        print(f"Insert a base {desc} in the range of 2 and 16 \n")
        base_int = prompt_input_number(2, 16)
    return base_int


def insert_number_in_base(base):
    digits = DIGITS[0:base]  # this is to check for valid input
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
        input_value = convert_to_decimal(input_base, str(input_value))

    return convert_from_decimal(output_base, int(input_value))


def convert_from_to_ui():
    from_base = select_base("to convert from")
    nb_to_convert = insert_number_in_base(from_base)
    to_base = select_base("to convert to")
    result = convert_from_to(from_base, to_base, nb_to_convert)
    print(f"{nb_to_convert} in base {from_base} is {result} in base {to_base}")


convert_from_to_ui()
