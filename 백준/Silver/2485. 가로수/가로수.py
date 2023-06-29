import sys
input = sys.stdin.readline

def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x    

arr = []
distance = []
for i in range(int(input())):
    arr.append(int(input()))
    if i != 0:
        distance.append(arr[i] - arr[i-1])

distance_set = list(set(distance))
m = distance_set[0]
for i in range (1, len(distance_set)):
    m = gcd(m, distance_set[i])

result = 0
for i in distance:
    result += (i//m) - 1

print(result)
