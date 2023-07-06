import sys
input = sys.stdin.readline

def mergeSort(arr, start, end): 
    if start >= end: return
    mid = (start + end) // 2 
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid + 1, end)
    if cnt == k :
        return
    
def merge(arr, start, mid, end):
    global cnt, result, k
    i, j = start, mid
    merged= []
    while i < mid and j <= end:
        if arr[i] <= arr[j]:
            cnt += 1
            if cnt == k :
                result = arr[i]
                return
            merged.append(arr[i])
            i += 1
        else :
            cnt += 1
            if cnt == k :
                result = arr[j]
                return
            merged.append(arr[j])
            j += 1
    while i < mid:
        cnt += 1
        if cnt == k :
            result = arr[i]
            return
        merged.append(arr[i])
        i += 1
    while j <= end:
        cnt += 1
        if cnt == k :
            result = arr[j]
            return
        merged.append(arr[j])
        j += 1
    
    idx = start
    for num in merged:
        arr[idx] = num
        idx += 1
    
n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt, result = 0, 0
mergeSort(arr, 0, len(arr)-1)
if k > cnt:
    print(-1)
else:    
    print(result)