def solution(book_time):
    arr = []
    for i in book_time:
        arr.append([int(i[0][0:2]) * 60 + int(i[0][3:5]), int(i[1][0:2]) * 60 + int(i[1][3:5]) + 10])
    arr.sort()
    cur = 1
    for i in range(1, len(arr)):
        tmp = 0
        for j in range(i):
            if arr[j][0] <= arr[i][0] < arr[j][1] or arr[j][0] < arr[i][1] <= arr[j][1]:
                tmp += 1
        cur = max(cur, tmp + 1)
    
    return cur