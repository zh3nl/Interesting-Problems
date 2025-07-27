def print_num(n):
    num = 1
    result = ""
    
    while num <= n:
        result = result + str(num)
        num += 1
    
    print(result)

if __name__ == '__main__':
    n = int(input())
    print_num(n)
