import sys
input = sys.stdin.readline

arr = []
s = input()
for i in range(len(s)-1):
    arr.append(int(s[i]))

arr.sort(reverse=True)
for i in arr:
    print(i, end='')
