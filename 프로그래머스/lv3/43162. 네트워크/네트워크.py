from collections import deque
def solution(n, computers):
    def bfs(start):
        cnt = 0
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for i in range(n):
                if computers[x][i] == 1 and not visit[i]:
                    visit[x] = True
                    queue.append(i)
                
    
    visit = [False] * n
    answer = 0
    for i in range(n):
        if not visit[i]:
            bfs(i)
            answer += 1
            
    
    return answer


