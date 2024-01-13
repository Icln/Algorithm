import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(input())
result = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if arr[j] == 'H':
                arr[j] = 0
                result += 1
                break
print(result)