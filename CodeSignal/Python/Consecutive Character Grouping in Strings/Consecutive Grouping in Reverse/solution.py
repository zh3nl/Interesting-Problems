def solution(s):
    # TODO: implement the algorithm to find consecutive groups of characters in the reverse order
    groups = []
    curr_group_char = None
    curr_group_len = 0
    
    for i in range(len(s) - 1, -1, -1):
        curr_char = s[i]
        
        if curr_char == curr_group_char:
            curr_group_len += 1
        else:
            if curr_group_char is not None:
                groups.append((curr_group_char, curr_group_len))
            curr_group_char = curr_char
            curr_group_len = 1
    
    if curr_group_char is not None:
        groups.append((curr_group_char, curr_group_len))
    
    return groups
