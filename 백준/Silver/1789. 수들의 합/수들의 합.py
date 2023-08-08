s = int(input())
total = 0
count = 0

while True:
    count += 1
    total += count
    if total > s:
        break

print(count-1)