def unusual_traversal(array):
    # TODO: implement this function
    mid = len(array) // 2
    left = mid - 1
    right = mid + 1
    result = [array[mid]]
    take_left = True
    
    while left >= 0 or right < len(array):
        if take_left:
            count = min(2, left + 1)
            for i in range(left - count + 1, left + 1):
                result.append(array[i])
            left -= count
        else:
            count = min(2, len(array) - right)
            for i in range(right, right + count):
                result.append(array[i])
            right += count
        
        take_left = not take_left
        
    return result
