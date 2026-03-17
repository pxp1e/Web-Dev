lst = []
n = int(input())
for _ in range(n):
    cmd = input().split()
    operation = cmd[0]
    if operation == "insert":
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif operation == "print":
        print(lst)
    elif operation == "remove":
        lst.remove(int(cmd[1]))
    elif operation == "append":
        lst.append(int(cmd[1]))
    elif operation == "sort":
        lst.sort()
    elif operation == "pop":
        lst.pop()
    elif operation == "reverse":
        lst.reverse()