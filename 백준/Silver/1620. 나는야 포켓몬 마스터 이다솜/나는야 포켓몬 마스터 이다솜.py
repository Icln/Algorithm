import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range (n):
    s = input().rstrip()
    dic[s] = i + 1
    dic[i+1] = s

for _ in range (m):
    req = input().rstrip()
    if req.isdigit():
        print(dic[int(req)])
    else:
        print(dic[req])