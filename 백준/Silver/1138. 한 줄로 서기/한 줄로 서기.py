n = int(input())
arr = list(map(int, input().split()))
result = [0] * n
for idx, val in enumerate(arr):
    tmp = 0
    cnt = 0
    while cnt < n - 1:
        if val == 0:
            break
        if result[cnt] == 0:
            tmp += 1
        cnt += 1
        if tmp == val:
            break
    while result[cnt] != 0:
        cnt += 1
    result[cnt] = idx + 1
    
print(*result)

