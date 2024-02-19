import sys
input = sys.stdin.readline
 
 
def nextPermutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return False
 
    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1
 
    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result
 
 
T = int(input())
for _ in range(T):
    _input = list(input().rstrip())
    answer = nextPermutation(_input)
    if not answer:
        print("".join(_input))
    else:
        print("".join(answer))