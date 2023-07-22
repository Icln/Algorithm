import sys
input = sys.stdin.readline
def divide(cnt, x_start, x_end, y_start, y_end):
    global w_result, b_result

    if cnt == 1:
        if board[x_start][y_start] == 1:
            b_result += 1
        else:
            w_result += 1
        return 
    
    temp = set()
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            temp.add(board[i][j])
    
    if len(temp) == 1:
        if list(temp)[0] == 1:
            b_result += 1
        else:
            w_result += 1
        return

    divide(cnt // 2, x_start, (x_start + x_end) // 2, y_start, (y_start + y_end) // 2) # 1
    divide(cnt // 2, x_start, (x_start + x_end) // 2, (y_start + y_end) // 2, y_end) # 2
    divide(cnt // 2, (x_start + x_end) // 2, x_end, y_start, (y_start + y_end) // 2) # 3
    divide(cnt // 2, (x_start + x_end) // 2, x_end, (y_start + y_end) // 2, y_end) # 4

n = int(input())
board = [list(map(int,input().split()))for _ in range(n)]
w_result, b_result = 0, 0
divide(n, 0, n, 0, n)
print(w_result)
print(b_result)