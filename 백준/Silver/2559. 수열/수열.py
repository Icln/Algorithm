import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = [sum(arr[:k])]
for i in range(1, n - k + 1):
    result.append(result[i - 1] - arr[i - 1] + arr[i + k - 1])
print(max(result))