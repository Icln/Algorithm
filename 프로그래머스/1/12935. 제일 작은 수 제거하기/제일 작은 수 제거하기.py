def solution(arr):
    m = min(arr)
    arr.remove(m)
    
    if not arr:
        arr.insert(0, -1)
    
    return arr