def solution(s):
    # TODO: Implement the solution here
    words = s.split(" ")
    rotated = []
    for word in words:
        rotated.append(word[-1] + word[:-1])
    
    return " ".join(rotated)
