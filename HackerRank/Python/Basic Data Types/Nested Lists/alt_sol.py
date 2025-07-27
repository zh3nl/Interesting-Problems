def print_second_lowest(record):
    scores = sorted(set([student[1] for student in record]))
    
    for student in sorted(record):
        if student[1] == scores[1]:
            print(student[0])
    
if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
    print_second_lowest(record)
        
