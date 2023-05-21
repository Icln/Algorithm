n = int(input())
arr = [[0 for _ in range(101)]for _ in range(101)]
result = 0

for _ in range(n):
    x,y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1
            
for i in range(101):
    result += arr[i].count(1)

print(result)
            