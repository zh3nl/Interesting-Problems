def print_avg(student_marks, query_name):
    mark_sum = 0.0
    for mark in student_marks[query_name]:
        mark_sum += mark
    result = mark_sum / len(student_marks[query_name])
    print(f"{result:.2f}")

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print_avg(student_marks, query_name)
