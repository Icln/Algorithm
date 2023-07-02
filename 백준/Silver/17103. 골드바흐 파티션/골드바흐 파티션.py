import sys
input = sys.stdin.readline

n = int(input())
num_list =[int(input()) for _ in range(n)]
prime = [True for _ in range(max(num_list) + 1)]

for i in range(2, int(max(num_list) ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, max(num_list) + 1, i):
            prime[j] = False

for num in num_list:
    result = 0
    for i in range (2, num//2 + 1):
        if prime[i] and prime[num - i]:
            result += 1    
    print(result)
