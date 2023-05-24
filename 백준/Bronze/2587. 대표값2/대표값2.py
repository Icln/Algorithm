arr = []
for _ in range(5):
    arr.append(int(input()))

result = sorted(arr)
print(sum(result)//5)
print(result[2])