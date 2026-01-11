def solution(input_str):
    # split the string into words
    words = input_str.split()
    
    # reverse each word 
    reversed_words = [''.join(reversed(word)) for word in words]
    
    # join the words back together with space as a separator
    result = ' '.join(reversed_words)
    
    return result

# Now we call the function and print the returned result outside of the function
print(solution("Hello neat pythonistas_123"))  # this will print: 'olleH taen 321_satsinohtyp'
