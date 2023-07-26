dp = dict()
p = 1000000007
dp[0], dp[1], dp[2] = 0, 1, 1
def fibo(n):
    if dp.get(n) != None:
        return dp[n]
    if n % 2 == 0:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % p 
        dp[n // 2 - 1] = fibo(n // 2 - 1) % p
        return (dp[n // 2 + 1] ** 2 % p) - (dp[n // 2 - 1] ** 2 % p)
    else:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % p
        dp[n // 2] = fibo(n // 2) % p
        return (dp[n // 2 + 1] ** 2 % p) + (dp[n // 2] ** 2 % p)

print(fibo(int(input())) % p)