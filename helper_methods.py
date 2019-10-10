def input_int(lower_limit=0, upper_limit=99999999999999999):
    input_str = input()
    input_int = -1
    try:
        input_int = int(input_str)
    except ValueError:
        print("Must insert a number")
        return None
    if lower_limit <= input_int <= upper_limit:
        return input_int
    else:
        print(f"Insert a number between {lower_limit} and {upper_limit}")
        return None

def input_float(lower_limit=0, upper_limit=99999999999999999):
    input_str = input()
    input_foat = -1
    try:
        input_float = float(input_str)
    except ValueError:
        print("Must insert a number")
        return None
    if lower_limit <= input_float <= upper_limit:
        return input_float
    else:
        print(f"Insert a number between {lower_limit} and {upper_limit}")
        return None