from itertools import product
n, k, p, x = map(int, input().split())
num = []
numbers = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
           [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
           [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
           [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

for i in range(1, k + 1):
    num.append(x % 10)
    x //= 10
num = num[::-1]

result = 0
idx = [i for i in range(10)]
for i in product(idx, repeat=k):
    cnt = 0
    tmp = ''
    for id, val in enumerate(i):
        cnt += numbers[num[id]][val]
        tmp += str(val)
    if cnt <= p and 1 <= int(tmp) <= n:
        result += 1
print(result - 1)