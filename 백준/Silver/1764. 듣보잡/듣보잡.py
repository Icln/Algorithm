import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
not_hear = set()
not_see = set()

for _ in range (n):
    not_hear.add(input().rstrip())
for _ in range (m):
    not_see.add(input().rstrip())

result = sorted(list(not_hear & not_see))
print(len(result))
for i in result:
    print(i)