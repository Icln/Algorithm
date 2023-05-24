n = int(input())
cnt = 0
num = 666
while True:
    if str(num).find("666") != -1:
        cnt += 1    
    if cnt == n: 
        print(num)
        break
    num+=1
   
    