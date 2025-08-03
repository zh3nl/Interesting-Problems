def solution(n):
    # TODO: implement
    odd_prod = 1
    found_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_prod *= digit
            found_odd = True
        
        n = n // 10
        
    return odd_prod if found_odd else 0
