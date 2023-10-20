answer = 0
def solution(n):
    def dfs(row, col):
        global answer
        if col in visit:
            return
        
        for i in visit:
            if abs(col - i) == abs(row - visit.index(i)):
                return
        
        if row == n - 1:
            answer += 1
            return
        for i in range(n):
            visit.append(col)
            dfs(row + 1 , i)
            visit.pop()  
        return 
    
    for i in range(n):
        visit = []
        dfs(0, i)
        
    return answer