N, B= map(int, input().split())
number ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while N:
    result += str(number[N%B])
    N //= B

print(result[::-1])