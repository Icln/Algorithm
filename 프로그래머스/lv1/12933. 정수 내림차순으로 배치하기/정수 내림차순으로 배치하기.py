def solution(n):
    return int("".join(sorted(list(str(int(n))), reverse = True)))