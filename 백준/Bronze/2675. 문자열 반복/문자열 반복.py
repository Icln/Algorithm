n = int(input())
for _ in range (n):
   cnt, s = input().split()
   for i in s:
      print(i * int(cnt), end='')
   print()