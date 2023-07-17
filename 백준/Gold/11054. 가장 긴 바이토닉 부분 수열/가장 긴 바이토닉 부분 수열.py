import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
rev = numbers[::-1]
dp_asc = [1] * n
dp_desc = [0] * n
for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)

for i in range(n):
    for j in range(i):
        if rev[j] < rev[i]:
            dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)

dp_desc.reverse()
for i in range(n):
    dp_asc[i] += dp_desc[i] 
print(max(dp_asc))
