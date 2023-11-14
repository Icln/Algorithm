for i in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    for j in range(n):
        if min(arr) == max(arr):
            break
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
            
    print(f'#{i + 1} {max(arr) - min(arr)}')
    