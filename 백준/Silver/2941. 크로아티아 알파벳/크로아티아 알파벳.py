arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()

for i in arr:
    s = s.replace(i, '!')
print(len(s))   