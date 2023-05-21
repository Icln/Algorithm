X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line % 2 == 0:
    a = X
    b = line + 1 - a
else:
    b = X
    a = line + 1 - b
        
print(f'{a}/{b}')