if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        command = input().split()
        cmd = command[0]
        if cmd == "insert":
            index, value = int(command[1]), int(command[2])
            lst.insert(index, value)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            value = int(command[1])
            lst.remove(value)
        elif cmd == "append":
            value = int(command[1])
            lst.append(value)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()