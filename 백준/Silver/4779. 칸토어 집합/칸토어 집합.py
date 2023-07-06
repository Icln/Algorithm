import sys
input = sys.stdin.readline
def cantoer(n, length, start):
    if length == 1:
        return
    distance = length // 3
    for i in range(start + distance, start + distance * 2):
        n[i] = ' '
    cantoer(n, distance, start) #start
    cantoer(n, distance, start + distance * 2) #end

while True:
    try :   
        n = list('-' * 3 ** int(input()))
        cantoer(n, len(n), 0)
        print(''.join(n))
    except :
        break