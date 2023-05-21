while True:
    n = int(input())
    if n == -1 :
        break
    arr = []
    for i in range(1,n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) != n:
        print(f'{n} is NOT perfect.')
    else :
        print(f'{n} =',end=' ')
        for i in (arr):
            if i == arr[len(arr)-1]:
                 print(f'{i}')
            else :
                print(f'{i} +', end=' ')
 