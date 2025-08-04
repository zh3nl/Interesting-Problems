def reversed_triple_chars(s: str) -> str:
    # TODO: Implement the function that reform the string as described above
    result = ''
    length = len(s)
    elem_count = 0
    temp = ''
    
    for i in range(length):
        temp += s[i]
        elem_count += 1
        
        if elem_count == 3:
            result += temp[::-1]
            elem_count = 0
            temp = ''
        
    result += temp
    return result
