from itertools import permutations
n, m = map(int,input().split())
arr = list(map(int,input().split()))
p = list(permutations(arr,3))

mx = 0
for i in p:
    if sum(i) >= mx and sum(i) <= m :
         mx = sum(i)

print(mx)