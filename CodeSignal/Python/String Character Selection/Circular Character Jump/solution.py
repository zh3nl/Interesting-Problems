def repeat_char_jump(inputString, k):
    # TODO: Implement the solution to generate n-length string as per given instructions.
    result = ''
    length = len(inputString)
    curr = 0
    
    for i in range(length):
        result += inputString[curr]
        curr = curr + k
        
        if curr >= length:
            curr = curr - length
    
    return result
