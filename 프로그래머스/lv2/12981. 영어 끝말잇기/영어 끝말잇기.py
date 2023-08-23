def solution(n, words):
    check = dict()
    check[words[0]] = True
    for i in range(1, len(words)):
        if check.get(words[i]) == None and words[i - 1][-1] == words[i][0]: 
            check[words[i]] = True
        else:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]
        