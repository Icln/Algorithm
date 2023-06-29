import sys
input = sys.stdin.readline

s = input().rstrip()
arr = set()
for i in range (len(s)):
    for j in range (i, len(s)):
        arr.add(s[i : j + 1])

print(len(arr))