def solution(files):
    s = []
    answer = []
    for i in files:
        head, number, tail = '', '', ''
        for j in i:
            if number == '' and not j.isdigit():
                head += j
            elif tail == '' and j.isdigit():
                number += j
            else:
                tail += j
        s.append([head.upper(), int(number), tail, files.index(i)])
    s.sort(key = lambda x : (x[0], x[1], x[3]))
    
    for i in range(len(files)):
        head, number, tail = '', '', ''
        for j in files[i]:
            if number == '' and not j.isdigit():
                head += j
            elif tail == '' and j.isdigit():
                number += j
            else:
                tail += j
        find = [head.upper(), int(number), tail, i]
        answer.append([s.index(find), files[i]]) 
    
    answer.sort(key = lambda x: x[0])
    return [i[1] for i in answer]