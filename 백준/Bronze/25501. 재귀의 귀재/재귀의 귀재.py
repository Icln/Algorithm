import sys
input = sys.stdin.readline

def recursion(s, l, r, cnt):
    if l >= r: return (1, cnt)
    elif s[l] != s[r]: return (0, cnt)
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for _ in range(int(input())):
    arr = list(isPalindrome(input().rstrip()))
    for i in arr:
        print(f'{i} ',end='')