def solution(arr):
    maximum = max(arr)
    arr.sort()
    tmp = maximum
    while True:
        flag = True
        for i in range(0, len(arr) - 1):
            if tmp % arr[i] != 0:
                flag = False
                break
        if flag:
            return tmp
        tmp += maximum
