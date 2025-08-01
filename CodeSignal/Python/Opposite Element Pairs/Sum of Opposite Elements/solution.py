def solution(numbers):
    # TODO: Implement solution here
    result = []
    n = len(numbers)
    
    left = 0
    right = n - 1
    while left <= right:
        result.append(numbers[left] + numbers[right])
        left += 1
        right -= 1
        
    return result
