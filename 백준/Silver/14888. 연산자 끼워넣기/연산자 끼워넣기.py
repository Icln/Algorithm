import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
cnt = list(map(int, input().split()))
operator = []
result = set()

for i in range(4):
    for j in range(cnt[i]):
        if i == 0:
            operator.append('+')
        elif i == 1:
            operator.append('-')
        elif i == 2:                
            operator.append('*')
        elif i == 3:
            operator.append('/')

def check(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return div(x,y)

def div(x, y):
    global flag
    if y == 0:
        flag = False
        return 
    if x < 0:
        return -(abs(x) // y)
    else: return x // y

s = sum(cnt)
new_operator = []
def dfs(n):
    if n == s:
        op = []
        for i in temp:
            op.append(operator[i])
        new_operator.append(op)
        return 

    for i in range(s):
        if i not in temp:
            temp.append(i)
            dfs(n+1)
            temp.pop()

temp = []
dfs(0)
flag = True
new_operator = [list(x) for x in set(tuple(row) for row in new_operator)]
for i in range(len(new_operator)):
    new_numbers = numbers[:]
    for j in range(n-1):
        cal = check(new_numbers[j], new_numbers[j+1], new_operator[i][j])
        if not flag:
            break
        else:
            new_numbers[j+1] = cal
    if flag:
        result.add(cal)
    else:    
        flag = True
print(max(result))
print(min(result))