# You need to develop a Python function, special_order(inputString), which takes inputString as an argument. The resulting string begins with the last character of the inputString, then selects the second-to-last character, continuing in reverse order until you reach the middle character of the string. Then, start with the first character of the inputString, proceed to the second character, and continue in this manner until you reach the middle character.

def special_order(inputString):
    # TODO: Implement function
    result = ''
    length = len(inputString)
    mid = length // 2 + length % 2
    
    for i in range(mid):
        result += inputString[length - 1 - i]
    
    for i in range(mid):
        if i != length - 1 - i:
            result += inputString[i]
    
    return result
