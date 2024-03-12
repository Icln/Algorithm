import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n - 1
tmp = abs(arr[l] + arr[r])
result = [arr[l], arr[r]]


while l < r:
    left = arr[l]
    right = arr[r]
    s = left + right
  
    if abs(s) < tmp:
        tmp = abs(s)
        result = [left, right]
        if tmp == 0:
          break
    if s < 0:
        l += 1
    else:
        r -= 1

print(result[0], result[1])