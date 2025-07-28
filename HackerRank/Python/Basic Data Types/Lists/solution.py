if __name__ == '__main__':
    N = int(input())
    cmds = []
    
    for i in range(N):
        cmd = input()
        cmds.append(cmd)
        
    cleaned_cmds = [cmd.split(" ") for cmd in cmds]
    output = []
    
    for cmd in cleaned_cmds:
        match cmd[0]:
            case "insert":
                output.insert(int(cmd[1]), int(cmd[2]))
            case "print":
                print(output)
            case "remove":
                output.remove(int(cmd[1]))
            case "append":
                output.append(int(cmd[1]))
            case "sort":
                output.sort()
            case "pop":
                output.pop()
            case "reverse":
                output.reverse()
            
