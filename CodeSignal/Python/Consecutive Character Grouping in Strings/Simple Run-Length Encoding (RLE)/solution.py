def encode_rle(s):
    # TODO: implement
    result = ""
    curr_group_char = None
    curr_group_len = 0
    
    for char in s:
        if char.isdigit() or char.isalpha():
            if char == curr_group_char:
                curr_group_len += 1
            else:
                if curr_group_char is not None:
                    result += f"{curr_group_char}{curr_group_len}"
                curr_group_char = char
                curr_group_len = 1
    
    if curr_group_char is not None:
        result += f"{curr_group_char}{curr_group_len}"
        
    return result
