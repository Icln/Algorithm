a = [0  for i in range(10)]
for i in range(0, 10):
   a[i] = int(input()) % 42

print(len(set(a)))