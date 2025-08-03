def solution(n):
    # TODO: implement
    consec_count = 0
    prev_digit = float('inf')
    
    while n > 0:
        curr_digit = n % 10
        
        if curr_digit == prev_digit:
            consec_count += 1
        
        prev_digit = curr_digit
        n = n // 10
    
    return consec_count
