import sys
input = sys.stdin.readline

n= int(input())
team = [list(map(int, input().split())) for i in range(n)]
numbers = [i for i in range(n)] 
min_result = int(1e9)

result1 = 0
result2 = 0

cnt = 1
for i in range(n//2 + 1 , n + 1):
    cnt*=i

for i in range(1, n//2 + 1):
    cnt//=i
cnt//= 2


def start_sum(start):
    global result1 
    if len(cal1) == 2:
        x1, y1 = cal1[0], cal1[1]
        result1 += team[x1][y1]
        result1 += team[y1][x1]
        return
    
    for k in range(start, len(temp)):
        if temp[k] not in cal1:
            cal1.append(temp[k])
            start_sum(k+1)
            cal1.pop()

def link_sum(start):
    global result2 
    if len(cal2) == 2:
        x2, y2 = cal2[0], cal2[1]
        result2 += team[x2][y2]
        result2 += team[y2][x2]
        return

    for k in range(start, len(temp)):
        if sub[k] not in cal2:
            cal2.append(sub[k])
            link_sum(k+1)
            cal2.pop()
def dfs(start):  
    global result1, result2, sub, cnt ,min_result
    if not cnt:
        return
    if len(temp) == n // 2:
        cnt -= 1
        sub = list(set(numbers) - set(temp))
        start_sum(0)
        link_sum(0)
        if min_result > abs(result1 -result2):
            min_result = abs(result1 -result2)
        result1 = 0
        result2 = 0
        return
    
    for k in range(start, n):
        if k not in temp:
            temp.append(k)
            dfs(k+1)
            temp.pop()

temp = []
cal1 = []
cal2 = []

dfs(0)
print(min_result)