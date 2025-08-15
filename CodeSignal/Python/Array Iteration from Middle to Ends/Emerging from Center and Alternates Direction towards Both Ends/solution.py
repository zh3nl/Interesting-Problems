def iterateMiddleToEnd(numbers):
    mid = len(numbers) // 2 # The index of the left middle element
    if len(numbers) % 2 == 1:
        left = mid - 1 # The left to the middle element
        right = mid + 1 # The right to the middle element
        new_order = [numbers[mid]] # Adding the middle element to the resulting array
    else:
        left = mid - 1 # Left middle element
        right = mid # Right middle element
        new_order = [] # No elements in the resulting array for now

    while left >= 0 and right < len(numbers):
        new_order.append(numbers[left])
        new_order.append(numbers[right])
        left -= 1
        right += 1
            
    return new_order
