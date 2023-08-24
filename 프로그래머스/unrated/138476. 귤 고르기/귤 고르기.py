from collections import Counter
def solution(k, tangerine):
    num = Counter(tangerine)
    arr = sorted([i[1] for i in num.items()])
    idx = 0 
    tmp = sum(arr)
    while k != tmp:
        arr[idx] -= 1 
        tmp -= 1
        if arr[idx] == 0:
            idx += 1
            
    return len(arr) - arr.count(0)