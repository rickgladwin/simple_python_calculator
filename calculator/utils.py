import numbers


"""Utilities to support the calculator package"""


def string_to_number(numberlike: str) -> numbers.Number:
    """converts an intlike or floatlike string to an int or float"""
    is_negative: bool = False
    absolute_numberlike = numberlike

    if numberlike[0] == '-':
        is_negative = True
        absolute_numberlike = numberlike.replace('-', '')

    if absolute_numberlike.isdigit() and is_negative:
        return 0 - int(absolute_numberlike)

    if absolute_numberlike.isdigit():
        return int(absolute_numberlike)

    if absolute_numberlike.replace('.', '').isdigit() and is_negative:
        return 0.0 - float(absolute_numberlike)

    if absolute_numberlike.replace('.', '').isdigit():
        return float(absolute_numberlike)

    raise ValueError(f'can only convert intlike or floatlike strings to number, got {numberlike}')

def string_list_to_numbers(args: list[str]) -> list[numbers.Number]:
    result = []
    for element in args:
        result.append(string_to_number(element))

    return result
