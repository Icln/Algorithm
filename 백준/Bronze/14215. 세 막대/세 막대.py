arr = sorted(map(int, input().split()))
result = arr[0] + arr[1] + min(arr[2], arr[0] + arr[1] - 1)
print(result)