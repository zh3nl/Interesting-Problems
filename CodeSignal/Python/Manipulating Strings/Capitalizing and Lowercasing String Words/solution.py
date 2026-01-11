def solution(input_str):
    # TODO: implement the function
    words = input_str.split()
    transformed = []
    
    for word in words:
        new_word = []
        for i in range(len(word)):
            if word[i].isalpha() and i == 0:
                new_word.append(word[i].upper())
            elif word[i].isalpha() and i != 0:
                new_word.append(word[i].lower())
            else:
                new_word.append(word[i])
        transformed.append("".join(new_word))
    
    return " ".join(transformed)
