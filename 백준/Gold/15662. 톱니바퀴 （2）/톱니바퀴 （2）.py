from collections import deque
t = int(input())
a = [0] + [deque(map(int,input().rstrip())) for _ in range(t)]
k = int(input())
r = [list(map(int, input().split())) for _ in range(k)]

for i, n in r:
    flag = []
    for j in range(i + 1, t + 1):
        if a[j][-2] != a[j - 1][2]:
            flag.append(j)
        else:
            break

    for j in range(i - 1, 0, -1):
        if a[j][2] != a[j + 1][-2]:
            flag.append(j)
        else:
            break

    a[i].rotate(n)
    for j in flag:
        a[j].rotate(-n if (j - i) % 2 else n)

result = sum([a[i][0] for i in range(1, t+1)])
print(result)