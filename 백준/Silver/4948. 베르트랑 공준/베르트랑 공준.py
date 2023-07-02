num = 123456*2+1
num_list = [1]*num
for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    
    if n == 0:
        break
    
    prime = 0
    for i in range(n+1, 2*n+1):
            prime += num_list[i]
    print(prime)