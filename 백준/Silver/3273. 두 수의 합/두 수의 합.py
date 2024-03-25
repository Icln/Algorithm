import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

answer=0
start = 0
end = n - 1

while start < end:
    cur = arr[start] + arr[end]
    if cur == x:
        answer += 1
        start += 1
    elif cur > x:
        end -= 1
    else:
        start += 1

print(answer)