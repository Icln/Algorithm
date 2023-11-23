from itertools import product

op = [' ', '+', '-']
for i in range(int(input())):
    n = int(input())
    for j in product(op, repeat=n-1):
        formula = ''
        for idx, val in enumerate(j):
            formula += str(idx + 1) + val
        formula += str(n)

        if eval(formula.replace(' ', '')) == 0:
            print(formula)
    print()
