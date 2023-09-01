
def solution(dirs):
    cur = [0, 0]
    move = {'U' : [0, 1], 'D': [0, -1], 'L' : [-1, 0], 'R' : [1, 0]}
    cnt = set()
    
    for i in dirs:
        if -5 <= cur[0] + move[i][0] <= 5 and -5 <= cur[1] + move[i][1] <= 5:
            cnt.add((cur[0], cur[1], cur[0] + move[i][0], cur[1] + move[i][1]))
            cnt.add((cur[0] + move[i][0], cur[1] + move[i][1], cur[0], cur[1]))
            cur[0] += move[i][0]
            cur[1] += move[i][1]
    return len(cnt) // 2