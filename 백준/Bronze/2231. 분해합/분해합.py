arr = []
n = int(input())
for i in range(n) : 
    tmp = i
    
    for j in str(i):
        tmp+= int(j)
    
    if tmp == n:
        arr.append(i)

if len(arr) == 0:
    print(0)
else :
    print(min(arr))