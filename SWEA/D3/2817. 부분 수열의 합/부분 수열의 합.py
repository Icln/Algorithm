from itertools import combinations
t = int(input())
for i in range(t):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0 
    for j in range(1, N + 1):
        for k in combinations(arr, j):
            if K == sum(k):
                result += 1
    print(f'#{i + 1} {result}')