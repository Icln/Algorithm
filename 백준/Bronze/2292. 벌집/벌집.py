n = int(input())
result = 1
cnt = 1
while n > cnt : 
    cnt += 6 * result
    result += 1
print(result)
