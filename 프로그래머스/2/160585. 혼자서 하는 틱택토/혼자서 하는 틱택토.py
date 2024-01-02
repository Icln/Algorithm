from collections import Counter

def game_set(c,board):
    for i in range(len(board)):
        if board[i][0] == c and board[i][1] == c and board[i][2] == c: 
            return True
        elif board[0][i] == c and board[1][i] == c and board[2][i] == c:
            return True
    if board[0][0] == c and board[1][1] == c and board[2][2] == c:
        return True
    elif board[0][2] == c and board[1][1] == c and board[2][0] == c:
        return True

def solution(board):
    counter = Counter(list(''.join(board)))
    if counter['X'] > counter['O'] or counter['X']+1 < counter['O']:
        return 0
    
    else:
        if game_set('O', board):
            if counter['O'] <= counter['X'] or game_set('X', board):
                return 0
            else:   
                return 1
        elif game_set('X', board):
            if counter['X'] < counter['O'] or game_set('O', board):
                return 0
            else:
                return 1
        else:
            return 1