import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
start, end = 1, k
result = 0

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    
    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)