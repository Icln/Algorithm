def solution(n):
    arr = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:      
                x += 1             
            elif i % 3 == 1:    
                y += 1
            elif i % 3 == 2:    
                x -= 1
                y -= 1      
            arr[x][y] = num
            num += 1
    
    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)
            
    return answer
    
    