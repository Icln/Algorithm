arr = []
for _ in range(5):
    arr.append(input())

for j in range(15):
    for i in range(5):
        if j < len(arr[i]):
            print(arr[i][j], end='')