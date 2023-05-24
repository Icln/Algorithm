n = int(input())
arr = []
for i in range(n):
    for j in range(n):
        if 3 * i + 5 * j == n:
            arr.append(i+j)
if len(arr) != 0:
    print(min(arr))
else :
    print(-1)