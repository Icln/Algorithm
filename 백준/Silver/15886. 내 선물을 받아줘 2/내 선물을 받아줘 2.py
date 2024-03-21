import sys
input = sys.stdin.readline

n, s = int(input()), input()
count = 0
for i in range(n-1):
    if s[i : i + 2] == 'EW': count += 1
print(count)