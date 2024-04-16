from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    one = deque(map(str, input().rstrip()))
    two = deque(map(str, input().rstrip()))
    three = deque(map(str, input().rstrip()))
    four = deque(map(str, input().rstrip()))
    k = int(input())
    arr = [list(map(int, input().split()))for _ in range(k)]

    for n, d in arr:
        if n == 1:
            if one[2] != two[6]:
                if two[2] != three[6]:
                    if three[2] != four[6]:
                        four.rotate(d * -1)
                    three.rotate(d)
                two.rotate(d * -1)
            one.rotate(d)
            continue
        if n == 2:
            if two[6] != one[2]:
                one.rotate(d * -1)
            if two[2] != three[6]:
                if three[2] != four[6]:
                    four.rotate(d)
                three.rotate(d * -1)
            two.rotate(d)
            continue
        if n == 3:
            if three[2] != four[6]:
                four.rotate(d * -1)
            if three[6] != two[2]:
                if two[6] != one[2]:
                    one.rotate(d)
                two.rotate(d * -1)
            three.rotate(d)
            continue
        if n == 4:
            if four[6] != three[2]:
                if three[6] != two[2]:
                    if two[6] != one[2]:
                        one.rotate(d * -1)
                    two.rotate(d)
                three.rotate(d * -1)
            four.rotate(d)
            continue

    print(int(one[0]) + int(two[0]) * 2 + int(three[0]) * 4 + int(four[0]) * 8)