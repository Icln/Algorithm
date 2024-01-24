import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

cur = max(dp)
start = dp.index(cur)
result = []

for i in range(start, -1, -1):
    if dp[i] == cur:
        result.append(arr[i])
        cur -= 1

print(len(result))
print(*result[::-1])