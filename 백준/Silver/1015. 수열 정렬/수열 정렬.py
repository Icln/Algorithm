n = int(input())
t = list(map(int, input().split()))
s_li = sorted(t)
li = []
for i in range(n):
    idx = s_li.index(t[i])
    li.append(idx)
    s_li[idx] = -1
print(*li)