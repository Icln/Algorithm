n = int(input())
s = format(n+1, 'b')
s = s[1:]
print(s.replace('0', '4').replace('1', '7'))