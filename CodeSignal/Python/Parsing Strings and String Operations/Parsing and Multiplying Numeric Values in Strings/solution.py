def parse_and_multiply_numbers(input_string):
    num = ""
    numbers = []
    for char in input_string:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""
    if num:
        numbers.append(int(num))
    result = 1
    for number in numbers:
        result *= number
    return result
