def solution(cards):
    def dfs(cur, tmp):
        if visit[cur - 1]:
            group.append(tmp)
            return
        visit[cur - 1] = True
        dfs(cards[cur - 1], tmp + 1)
    
    visit = [False] * len(cards)
    group = []
    
    for i in range(len(cards)):
        if not visit[i]:
            dfs(cards[i], 0)
    group.sort(reverse = True)
    return 0 if len(group) == 1 else group[0] * group[1] 
    
    
    