n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = sorted(arr)

for i in result:
    print(i)