def solution(numbers):
    # TODO: Implement the solution here
    mid = len(numbers) // 2
    
    if len(numbers) % 2 == 1:
        left = mid - 1
        right = mid + 1
        result = [numbers[mid]]
    else:
        left = mid - 1
        right = mid
        result = []
        
    while left >= 0 and right <= len(numbers):
        result.append(numbers[left] * numbers[right])
        left -= 1
        right += 1
        
    return result
    
