import math

def solution(numbers):
    # TODO: implement this function
    result = []
    n = len(numbers)
    
    for i in range(n):
        a = numbers[i]
        b = numbers[n - i - 1]
        
        geo_mean = round(math.sqrt(a * b), 2)
        result.append((numbers[i], geo_mean))
    
    return result
