def solution(s):
    # TODO: Implement the function here
    result = ""
    curr_group_pair = ""
    curr_group_len = 0 
    
    for i in range(0, len(s), 2):
        j = i + 2
        pair = s[i:j]
        
        if pair == curr_group_pair:
            curr_group_len += 1
        else:
            if curr_group_pair != "":
                result += f"{curr_group_pair}{curr_group_len}"
            curr_group_pair = pair
            curr_group_len = 1
    
    if curr_group_pair != "":
        result += f"{curr_group_pair}{curr_group_len}"
    
    return result
        
