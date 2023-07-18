import sys
input = sys.stdin.readline

s = '0' + input().rstrip()
n = int(input())

memo = [[0] * (len(s)+1) for i in range(26)]


diff = ord('a')
for i in range(1, len(s)):
    for j in range(26):
        if ord(s[i]) - diff == j:
            memo[j][i] = memo[j][i-1] + 1
        else:
            memo[j][i] = memo[j][i-1]
for i in range(n):
    alph, l, r = input().split()
    l, r = map(int, (l, r))
    print(memo[ord(alph)-diff][r+1]-memo[ord(alph)-diff][l])