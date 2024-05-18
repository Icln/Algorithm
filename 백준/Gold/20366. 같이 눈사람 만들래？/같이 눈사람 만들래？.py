import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    snow = list(map(int, input().split()))
    snow.sort()
    answer = 1e9

    for i in range(n - 3):
        for j in range(i + 3, n):
            anna = snow[i] + snow[j]

            k = i + 1
            l = j - 1

            while k < l:
                elsa = snow[k] + snow[l]
                check = anna - elsa

                if check > 0:
                    k += 1

                elif check < 0:
                    l -= 1

                elif check == 0:
                    print(0)
                    exit()

                check = check if check > 0 else -check
                answer = min(answer, check)

    print(answer)