from itertools import product
def solution(word):
    alpha = set()
    for i in range(5, 0, -1):
        for j in product("AEIOU", repeat = i):
            alpha.add(''.join(map(str, j)))
    
    alpha = sorted(list(alpha))
    return alpha.index(word) + 1
    