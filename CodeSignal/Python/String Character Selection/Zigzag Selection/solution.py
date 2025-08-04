def solution(inputString):
    result = ''
    length = len(inputString)
    for i in range(length // 2 + length % 2):
        result += inputString[i]
        if length - 1 - i != i:
            result += inputString[length - 1 - i]
    return result
