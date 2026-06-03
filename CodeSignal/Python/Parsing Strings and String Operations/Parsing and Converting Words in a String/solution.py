def solution(s):
    # TODO: Implement the function that could solve the task
    result = ""
    intermediate_digits = ''
    for char in s:
        if char == '-':
            if intermediate_digits != '':
                digits = int(intermediate_digits)
                letter = chr(ord('a') + digits - 1)
                result += letter
                intermediate_digits = ''
            result += char
        elif char.isdigit():
            intermediate_digits += char
        else:
            num = ord(char) - ord('a') + 1
            result += str(num)
    if s[-1].isdigit():
        digits = int(intermediate_digits)
        letter = chr(ord('a') + digits - 1)
        result += letter
    
    return result
