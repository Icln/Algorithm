a = []
for i in range(0,9):
   a.append(int(input()))
m = max(a)
for i in range(0,9):
   if a[i] == m:
      print(m)
      print(i+1)