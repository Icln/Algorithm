arr = [1, 1, 2, 2, 2, 8]
i = list(map(int,input().split()))
for j in range(0,6):
    print(arr[j] - i[j], end= " ")