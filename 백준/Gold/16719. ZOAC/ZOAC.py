import sys
input =sys.stdin.readline  

arr = list(input().rstrip())

result = [""]*len(arr)

def solution(start,arr):
    if not arr:
        return
    min_val = min(arr)
    temp = arr.index(min_val)
    
    result[start + temp] = min_val
    print("".join(result))
    solution(start+temp+1,arr[temp+1:]) 
    solution(start,arr[:temp])

solution(0,arr)
