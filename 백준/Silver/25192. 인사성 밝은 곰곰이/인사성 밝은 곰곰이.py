import sys
input = sys.stdin.readline

n = int(input())
arr = set()
result = 0
for i in range(n):
    str = input().rstrip()
    if str != 'ENTER':
        arr.add(str)
    else :
        result += len(arr)
        arr = set()
result += len(arr)        
print(result)