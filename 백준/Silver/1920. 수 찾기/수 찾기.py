import sys
input = sys.stdin.readline

n = int(input())
A = sorted(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def bs(start, end, m):
    if start > end:
        return 0
    
    pivot = (start + end) // 2
    if m == A[pivot]:
        return 1
    elif m < A[pivot]:
        return bs(start, pivot - 1, m)
    else: 
        return bs(pivot + 1, end, m)
        
for num in B:
   print(bs(0, n - 1, num)) 
