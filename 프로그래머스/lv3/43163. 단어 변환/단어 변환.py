from collections import deque
def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    queue.append([begin, 0])
    visit = [False for i in range(len(words))]
    
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            tmp = 0
            if not visit[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    queue.append([words[i], cnt+1])
                    visit[i] = True
    return answer