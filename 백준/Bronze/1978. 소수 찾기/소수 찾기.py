import math
n = int(input())
arr = list(map(int, input().split()))

result = 0

for i in arr:
    check = True
    if i == 1:
        pass 
    elif i == 2:
        result+=1
        pass
    elif i == 3:
        result +=1
        pass
    elif i % 2 == 0:
        pass
    else:
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                check = False
                break
        if check :
            result += 1    

print(result)            