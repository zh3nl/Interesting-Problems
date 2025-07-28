# Note, this problem only works in Python 2 due to Python 3's hash randomization
if __name__ == '__main__':
    n = int(raw_input())
    int_list = map(int, raw_input().split())
    t = tuple(int_list)
    print(hash(t))
