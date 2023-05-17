n, x = map(int, input().split())
n_list = list(map(int, input().split()))
for i in range(0,n):
   if (n_list[i] < x):
      print(n_list[i], end = " ")