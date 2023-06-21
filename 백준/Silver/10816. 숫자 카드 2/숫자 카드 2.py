import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
temp = list(map(int,input().split()))

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] +=1
    else:
        cnt[card] = 1
        
for i in temp:
   result = cnt.get(i)
   if result == None: 
       print(0, end=" ")
   else:
       print(result, end=" ")
