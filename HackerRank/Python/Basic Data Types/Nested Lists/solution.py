def print_second_lowest(record):
    map = {}
    for pair in record:
        if pair[1] not in map:
            map[pair[1]] = [pair[0]]
        else:
            map[pair[1]].append(pair[0])
    keys_list = list(set(map.keys()))
    keys_list.sort()
    second_highest = keys_list[1]
    
    second_highest_names = map[second_highest]
    second_highest_names.sort()
    for name in second_highest_names:
        print(name)

if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
    print_second_lowest(record)
        
