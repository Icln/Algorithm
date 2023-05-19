c = int(input())
for _ in range(c):
    cnt = 0
    arr = list(map(int,input().split()))
    avg = (sum(arr) - arr[0]) / arr[0]
    for i in range(1, arr[0] + 1):
        if arr[i] > avg:
            cnt += 1
    result = cnt/arr[0]*100   
    print(f'{result:.3f}%')  

    