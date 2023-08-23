def solution(brown, yellow):
    carpet = []
    sum = brown + yellow
    for i in range(sum, 0, -1):
        if sum % i == 0:
            height = sum // i
            width = sum // height
            if width >= height and height >= 3:
                carpet.append([width, height])
    
    for i in carpet:
        if yellow % (i[1] - 2) == 0:
            yellowWidth = yellow // (i[1] - 2)
            yellowHeight = yellow // yellowWidth + 2
            if yellowWidth + 2 == i[0] and yellowHeight == i[1]:
                return i