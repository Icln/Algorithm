import math
n = int(input())
m = int(input())

result = 0
arr = []
for i in range(n,m+1):
    check = True
    if i == 1:
        pass 
    elif i == 2:
        arr.append(2)
        pass
    elif i % 2 == 0:
        pass
    else:
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                check = False
                break
        if check:
            arr.append(i)
if len(arr) != 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)            