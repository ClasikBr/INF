lst = [int(x) for x in input().split()]
cmd = input().strip()

let = cmd[0]
num = int(cmd[1:])

ln = len(lst)
num %= ln

if let == 'R':
    lst = lst[-num:] + lst[:-num]
else:
    lst = lst[num:] + lst[:num]

print(lst)
