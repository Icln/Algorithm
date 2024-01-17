def solution(n, tops):
    case = [[0] * 2 for _ in range(100001)]
    case[0][0] = 1
    mod = 10007
    
    for i in range(n):
        case[i + 1][0] = case[i][0] * (2 + tops[i]) + case[i][1] * (1 + tops[i])
        case[i + 1][1] = case[i][0] + case[i][1]
        
        case[i + 1][0] %= mod
        case[i + 1][0] %= mod
        
    return (case[n][0] + case[n][1]) % mod