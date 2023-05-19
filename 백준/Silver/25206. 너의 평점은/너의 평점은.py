grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
g = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

s = 0
total = 0
for _ in range(20):
    x,y,z = input().split()
    y = float(y)
    if z != 'P':
        s += y
        total += y *  g[grade.index(z)]
result = total / s
print(f'{result:.6f}')