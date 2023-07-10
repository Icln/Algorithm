import sys 
input = sys.stdin.readline
n = int(input())

def queen(row, col):
    global result
    if col not in visited:
        for i in visited:
            if abs(col - i) == abs(row - visited.index(i)):
                return
        visited.append(col)
        if row == n - 1:
            result += 1
            visited.pop()
            return 
        for i in range(n):
            queen(row + 1 , i)
        visited.pop()  
    else: 
        return 

result = 0
for i in range(n):
    visited = []
    queen(0, i)
    
print(result)