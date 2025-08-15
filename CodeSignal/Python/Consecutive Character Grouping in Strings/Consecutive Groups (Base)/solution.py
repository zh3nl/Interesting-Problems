def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0

    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    groups.append((current_group_char, current_group_length))
                current_group_char = char
                current_group_length = 1
    if current_group_char is not None:
        groups.append((current_group_char, current_group_length))
    
    return groups
