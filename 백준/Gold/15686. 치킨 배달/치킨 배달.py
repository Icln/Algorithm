import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
one = []
two = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            one.append([i, j])
        elif arr[i][j] == 2:
            two.append([i, j])


d =[]
def dfs(idx, cnt):
    if cnt == m:
        result = 0
        for i in one:
            min_value = sys.maxsize
            for j in temp_two:
                distance = (abs(i[0] - two[j][0]) + abs(i[1] - two[j][1]))
                min_value = min(min_value, distance)
            result += min_value
        d.append(result)   
        return 

    for i in range(idx, len(two)):
        if i not in temp_two:
            temp_two.append(i)
            dfs(i + 1, cnt + 1)
            temp_two.pop()

temp_two = []        

dfs(0,0)
print(min(d))