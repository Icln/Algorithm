def check(arr, figure):
    if arr[0][0] == arr[0][1] == arr[0][2] == figure:
        return True
    if arr[1][0] == arr[1][1] == arr[1][2] == figure:
        return True
    if arr[2][0] == arr[2][1] == arr[2][2] == figure:
        return True
    if arr[0][0] == arr[1][0] == arr[2][0] == figure:
        return True
    if arr[0][1] == arr[1][1] == arr[2][1] == figure:
        return True
    if arr[0][2] == arr[1][2] == arr[2][2] == figure:
        return True
    if arr[0][0] == arr[1][1] == arr[2][2] == figure:
        return True
    if arr[2][0] == arr[1][1] == arr[0][2] == figure:
        return True
    return False

while True:
    s = input()
    if s == "end":
        break
    board = [[s[i * 3 + j] for j in range(3)] for i in range(3)]
    o, x = s.count('O'), s.count('X')
    if o > x:
        print("invalid")
        continue
    if x - o > 1:
        print("invalid")
        continue
    if x <= 2:
        print("invalid")
        continue
    if x == o:
        if check(board, 'O') and not check(board, 'X'):
            print("valid")
            continue
    if x == o + 1:
        if not check(board, 'O') and check(board, 'X'):
            print("valid")
            continue
    if x == 5 and o == 4:
        if not check(board, 'O'):
            print("valid")
            continue
    print("invalid")