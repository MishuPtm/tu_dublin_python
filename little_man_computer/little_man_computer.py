"""
Ionut Petrescu
Date: 20.11.2019
This is an interpreter for Little man computer logic

Example scripts:
Returns difference between two numbers:
00,901\n01,310\n02,901\n03,311\n04,210\n05,808\n06,510\n07,211\n08,902\n09,000\n10,000\n11,000

Add 2 numbers:
00,901\n01,399\n02,901\n03,199\n04,902\n05,000\n99,000
"""


def load_instructions(path):
    output = {}
    counter = 0
    try:
        with open(path, "r") as f:
            for line in f:
                if "," in line:
                    params = line.strip().split(",")
                    output[int(params[0])] = params[1]
                    counter += 1
                else:
                    output[counter] = line.strip()
                    counter += 1
        return output
    except IOError as e:
        for line in path.split("\n"):   # In case a string of commands was provided
            if "," in line:
                params = line.strip().split(",")
                output[int(params[0])] = params[1]
                counter += 1
            else:
                output[counter] = line
                counter += 1

        return output
        print(e)


def execute_instructions(instructions):
    counter = -1
    accumulator = 0
    while True:
        counter += 1
        action = instructions[counter][:1]
        address = int(instructions[counter][1:])
        if action == "1":       # add
            accumulator += int(instructions[address])
        elif action == "2":     # subtract
            accumulator -= int(instructions[address])
        elif action == "3":     # storing value to address
            instructions[address] = f"{accumulator:03}"
        elif action == "5":     # load
            if address in instructions.keys():
                accumulator = int(instructions[address])
            else:
                instructions[address] = "000"
                accumulator = "000"
        elif action == "6":     # jump
            counter = address - 1
        elif action == "7":     # branch on 0
            if accumulator == 0:
                counter = address - 1
        elif action == "8":     # branch on +
            if accumulator >= 0:
                counter = address - 1
        elif action == "9":       # input/output
            if address == 1:
                accumulator = int(input("Insert a number "))
            elif address == 2:
                print(accumulator)
        elif action == "0" and address == 0:    # STOP
            break


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


def show_interface(extension):
    import glob
    files = glob.glob(f"*.{extension}")
    if len(files) > 0:
        print("Select a file to run")
        for file in files:
            print(f"{files.index(file)+1} - {file}")
        selection = prompt_input_number(1, len(files))
        return files[selection-1]


def main():
    instructions = load_instructions(show_interface("txt"))
    execute_instructions(instructions)


if __name__ == "__main__":
    main()
