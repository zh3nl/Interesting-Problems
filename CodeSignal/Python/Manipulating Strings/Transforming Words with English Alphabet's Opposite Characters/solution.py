def solution(input_str):
    # TODO: implement the string transformation function
    words = input_str.split()
    replaced = []
    
    for word in words:
        new_word = "".join(replace_char(c) for c in word)
        replaced.append(new_word)
        
    return " ".join([replaced[-1]] + replaced[:-1])
    

def replace_char(char):
    if 'a' <= char <= 'z':
        return chr(ord('a') + ord('z') - ord(char))
    elif 'A' <= char <= 'Z':
        return chr(ord('A') + ord('Z') - ord(char))
    else:
        return char
