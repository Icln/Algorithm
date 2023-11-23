h, w = map(int, input().split())
heights = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    left = max(heights[:i])
    right = max(heights[i + 1:])

    if heights[i] < min(left, right):
        answer += min(left, right) - heights[i]

print(answer)