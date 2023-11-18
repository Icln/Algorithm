t = int(input())

for i in range(t):
    result = 0
    n = int(input())
    tmp, left, right = n // 2, 0, 0
    arr = [list(map(int, input().rstrip())) for _ in range(n)]
    for j in range(n):
        result += arr[j][tmp]
        for l in range(1, left + 1):
            result += arr[j][tmp - l]
        for r in range(1, right + 1):
            result += arr[j][tmp + r]

        if tmp > j:
            left += 1
            right += 1
        else:
            left -= 1
            right -= 1
    print(f'#{i+1} {result}')