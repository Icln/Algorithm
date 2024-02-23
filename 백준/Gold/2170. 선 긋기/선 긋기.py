import sys
input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

x, y = arr[0]
result = 0
for i in range(1, n):
    a, b = arr[i]
    if y > a:
        y = max(y, b)
    else:
        result += (y - x)
        x, y = a, b
    
print(result + (y - x))