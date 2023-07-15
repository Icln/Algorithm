import sys
d = [0] * 41

d[1] = 1
d[2] = 1
n= int(input())
cnt = 0
for i in range(3, n+1):
    cnt +=1
    d[i] = d[i- 1] + d[i - 2]

print(d[n], cnt)  