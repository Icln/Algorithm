n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = sorted(arr)
print(result[n-k])