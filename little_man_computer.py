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
    try:
        with open(path, "r") as f:
            for line in f:
                params = line.strip().split(",")
                output[int(params[0])] = params[1]

        return output
    except IOError as e:
        for line in path.split("\n"):   # In case a string of commands was provided
            params = line.strip().split(",")
            output[int(params[0])] = params[1]

        return output
        print(e)


def execute_instructions(instructions):
    counter = -1
    value = 0
    while True:
        counter += 1
        action = instructions[counter][:1]
        address = int(instructions[counter][1:])
        if action == "1":       # add
            value += int(instructions[address])
        elif action == "2":     # subtract
            value -= int(instructions[address])
        elif action == "3":     # storing value to address
            instructions[address] = f"{value:03}"
        elif action == "5":     # load
            value = int(instructions[address])
        elif action == "6":     # jump
            counter = address - 1
        elif action == "7":     # branch on 0
            if value == 0:
                counter = address - 1
        elif action == "8":     # branch on +
            if value > 0:
                counter = address - 1
        if action == "9":       # input/output
            if address == 1:
                value = int(input("Insert a number "))
            elif address == 2:
                print(value)
        elif action == "0" and address == 0:    # STOP
            break


def main():
    difference_2_nb = "00,901\n01,310\n02,901\n03,311\n04,210\n05,808\n06,510\n07,211\n08,902\n09,000\n10,000\n11,000"
    add_2_nb = "00,901\n01,399\n02,901\n03,199\n04,902\n05,000\n99,000"
    instructions = load_instructions(difference_2_nb)
    execute_instructions(instructions)


if __name__ == "__main__":
    main()
