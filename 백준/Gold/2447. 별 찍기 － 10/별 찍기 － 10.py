import sys
input = sys.stdin.readline
def star(n):
    if n == 1:
        return '*'
    temp = star(n//3)
    stars = []

    for i in temp:
        stars.append(i * 3)
    
    for i in temp:
        stars.append(i + ' ' * (n//3)+ i)
    
    for i in temp:
        stars.append(i * 3)
    return stars

result = star(int(input()))
for i in result:
    print(i)