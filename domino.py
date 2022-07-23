import argparse
from multiprocessing.sharedctypes import Value


DOMINOES = ['/', '|', '\\']
DOMINOES_SEQ = r'/\|'


def flip(char: str, turn: str):
    if turn == "prev":
        if char == "/":
            return "/", True
    else:
        if char == "\\":
            return "\\", True
    
    return "|", False


def domino_falling(input_variable: str, type_: str, iterations: int):
    if iterations < 0:
        raise ValueError

    result = []
    if type_ == "forward":
        for i in range(0, iterations):
            flipped_str = ''
            index = 0
            for char in input_variable:
                prev = input_variable[index - 1] if index != 0 else ""
                next = input_variable[index + 1] if index != len(input_variable) - 1 else ""
                if char == "|":
                    new_char, flipped = flip(prev, "prev")
                    if not flipped:
                        new_char, flipped = flip(next, "next")
                    
                    flipped_str += new_char
                else:
                    flipped_str += char
                
                index += 1
            input_variable = flipped_str
            result.append(input_variable)

    if type_ == "reverse":
        for i in range(0, iterations):
            str_array = [char for char in input_variable]
            flipped = False
            for i, char in enumerate(str_array):
                if i + 1 != len(input_variable):
                    if char == "/" and str_array[i + 1] != "/":
                        str_array[i] = "|"
                if i - 1 != -1:
                    if char == "\\" and str_array[i - 1] != "\\" and not flipped:
                        str_array[i] = "|"
                        flipped = True

            input_variable = "".join(str_array)
            result.append(input_variable)

    return result


def valid_input(input_: str):
    if not len(input_):
        raise ValueError

    diff = set(input_) - set(DOMINOES_SEQ)
    if diff:
        raise ValueError


def manage_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=str, required=True)
    parser.add_argument(
        "-t", type=str, required=True, choices=["forward", "reverse"]
    )
    parser.add_argument(
        "-i", type=int, required=True
    )

    args = parser.parse_args()

    input_variable = args.s
    type_ = args.t
    iterations = args.i

    try:
        valid_input(input_variable)
        res = domino_falling(input_variable, type_, iterations)
        for item in res:
            print(item)
    except ValueError as e:
        print("Invalid input value")
