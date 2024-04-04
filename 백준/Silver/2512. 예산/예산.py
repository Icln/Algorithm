N = int(input())
lst = list(map(int, input().split()))
M = int(input())
result = 0 
start, end = 1, max(lst) 
while start <= end:
    mid = (start + end) // 2 
    total = 0  
    for l in lst:
        if l > mid:
            total += mid
        else:
            total += l
    if total <= M:  
        result = mid
        start = mid + 1
    else:  
        end = mid - 1
print(result)