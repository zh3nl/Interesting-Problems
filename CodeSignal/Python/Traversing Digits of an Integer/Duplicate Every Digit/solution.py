def solution(n):
    # TODO: Implement the solution
    result = 0
    need_dupe = True
    digit_counter = 0
    
    while n > 0:
        digit = n % 10
        result += digit * (10 ** digit_counter)
        digit_counter += 1
        
        if need_dupe:
            result += digit * (10 ** digit_counter)
            digit_counter += 1
        
        n = n // 10
        
    return result
