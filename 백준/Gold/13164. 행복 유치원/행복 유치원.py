import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
diff = sorted([heights[i] - heights[i-1] for i in range(1, len(heights))])
print(sum(diff[:n-k]))