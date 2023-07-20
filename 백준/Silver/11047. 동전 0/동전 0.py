import sys
input = sys.stdin.readline
n, k = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

result = 0
for num in reversed(numbers):
    if k // num > 0:
        temp = (k // num)
        result += temp
        k -= (temp * num)
    elif k == 0:
        break            
print(result)
