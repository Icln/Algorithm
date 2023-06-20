n, m = map(int, input().split())
dic = {}
for _ in range (n):
    dic[input()] = 1

res = 0
for i in range (m):
    str = input()
    if(dic.get(str)==1):
        res +=1

print(res)
    
    