def solution(numbers):
    # TODO: implement solution here
    result = []
        
    for num in numbers:
        reversed_num = str(num)[::-1]
        
        if int(reversed_num) in numbers:
            result.append((num, numbers[numbers.index(int(reversed_num))]))
    
    return result
