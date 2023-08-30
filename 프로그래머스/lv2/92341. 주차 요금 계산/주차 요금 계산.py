import math
def solution(fees, records):
    tmp = dict()
    answer = []
    records.sort(key = lambda x : x[6:10])
    for i in range(len(records) - 1):
        time = 0
        if records[i][11] == 'O':
            continue        
        
        if records[i][6:10] == records[i + 1][6:10]:
            time += (int(records[i + 1][:2]) * 60 + int(records[i + 1][3:5]))
        else:
            time += 1439  
        time -= (int(records[i][:2]) * 60 + int(records[i][3:5]))
        
        if tmp.get(records[i][6:10]) == None:
            tmp[records[i][6:10]] = time
        else:
            tmp[records[i][6:10]] += time
    
    if records[-1][11] == 'I':
        if tmp.get(records[-1][6:10]) == None:
            tmp[records[-1][6:10]] = 1439 - (int(records[-1][:2]) * 60 + int(records[-1][3:5]))
        else:
            tmp[records[-1][6:10]] += 1439 - (int(records[-1][:2]) * 60 + int(records[-1][3:5]))
    
    for i in tmp.values():
        if i <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((i - fees[0])/fees[2]) * fees[3])
    
    return answer