n = int(input())
result = n
for _ in range(n):
    s = input()
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            result -=1
            break;

print(result)                        