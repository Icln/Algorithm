x = int(input())
n = int(input())
temp = 0
for i in range(n):
    a,b = map(int,input().split())
    temp += a*b
if temp == x :
    print("Yes")
else :
    print("No")