import numbers
from enum import Enum

from utils import string_list_to_numbers

"""Prompts the user for an operation and a list of int or float values,
 then performs the operation on the list and displays the result"""


def add(inputs: list[numbers.Number]) -> numbers.Number:
    total: numbers.Number = 0
    for number in inputs:
        total += number

    return total


def subtract(inputs: list[numbers.Number]) -> numbers.Number:
    total: numbers.Number = inputs[0]
    for i in range(1,len(inputs)):
        total -= inputs[i]

    return total


def multiply(inputs: list[numbers.Number]) -> numbers.Number:
    if 0 in inputs:
        return 0
    total: numbers.Number = 1
    for number in inputs:
        total *= number

    return total


def divide(inputs: list[numbers.Number]) -> numbers.Number:
    divisors = inputs[1:]
    if 0 in divisors:
        raise ValueError("Input list of numbers included zero. Can't divide by zero.")
    if inputs[0] == 0:
        return 0

    total: numbers.Number = inputs[0]
    for i in range(1,len(inputs)):
        total /= inputs[i]

    return total


class Operations(Enum):
    """Operations this module can handle, with a tuple containing
     each operation's function reference and name"""
    ADD = (add, "addition")
    SUBTRACT = (subtract, "subtraction")
    MULTIPLY = (multiply, "multiplication")
    DIVIDE = (divide, "division")


def calculate(operation, args: list) -> numbers.Number:
    result = operation(args)
    return result


def run() -> str:
    print('Calculator running.')
    print('Please select a calculation type:')
    calc_type_prompt: str = (f"1. {Operations.ADD.value[1]}\n"
                             f"2. {Operations.SUBTRACT.value[1]}\n"
                             f"3. {Operations.MULTIPLY.value[1]}\n"
                             f"4. {Operations.DIVIDE.value[1]}\n"
                             f"5. (Quit)\n"
                             "selection: ")

    selection: str = input(calc_type_prompt)

    match selection:
        case '1':
            operation = Operations.ADD
        case '2':
            operation = Operations.SUBTRACT
        case '3':
            operation = Operations.MULTIPLY
        case '4':
            operation = Operations.DIVIDE
        case '5' | 'Q':
            return 'Q'
        case _:
            raise RuntimeError(f"Received a selection that couldn't be handled: {selection}")

    print(f'Please enter a comma-separated list of numbers (int or float) for {operation.value[1]}')

    input_numbers: str = input()

    input_list: list[numbers.Number] = string_list_to_numbers(input_numbers.replace(' ', '').split(','))

    result: numbers.Number = calculate(operation.value[0], input_list)

    print(f'result of {operation.value[1]}: {result}')

    end_choice: str = input("Press Enter to calculate again, Q to quit: ")

    return end_choice

if __name__ == "__main__":
    quit_selected = False
    while not quit_selected:
        end_selection = run()
        if end_selection in ['Q', 'q', 'Quit', 'quit']:
            quit_selected = True
            print("Bye!")
