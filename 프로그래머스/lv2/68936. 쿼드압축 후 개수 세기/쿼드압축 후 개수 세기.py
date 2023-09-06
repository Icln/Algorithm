def solution(arr):
    answer = [0, 0]
    def dfs(x, y, size):
        if size == 1:
            answer[arr[x][y]] += 1
            return
        
        half = size // 2
        cur = arr[x][y]
        flag = True
        
        for i in range(x, x + size):
            for j in range(y, y + size):
                if cur != arr[i][j]:
                    flag = False
                    break
                    
        if flag:
            answer[cur] += 1
        else:
            dfs(x, y, half)
            dfs(x + half, y, half)
            dfs(x, y + half, half)
            dfs(x + half, y + half, half)
    
    dfs(0, 0, len(arr))
    return answer

        
        