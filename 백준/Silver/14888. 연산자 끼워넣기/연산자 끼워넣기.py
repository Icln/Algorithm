import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, cal, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, cal)
        min_result = min(min_result, cal)
        return
    if add:
        dfs(add - 1, sub, mul, div, cal + numbers[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, cal - numbers[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, cal * numbers[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(cal / numbers[idx]), idx + 1)

dfs(add, sub, mul, div, numbers[0], 1)
print(max_result)
print(min_result)