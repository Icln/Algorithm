def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    rows = zip(range(row_begin, row_end + 1), data[row_begin - 1 : row_end])
    
    for idx, row in rows:
        tmp = 0
        for col in row:
            tmp += col % idx
        answer ^= tmp

    return answer
    