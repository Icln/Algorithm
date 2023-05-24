n, m = map(int,input().split())
arr_b = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
arr_w = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

arr = []
for _ in range(n):
    arr.append(input())

result_b = []
result_w = []

for i in range(0, n-7):
    for j in range(0, m-7):
        num_b = 0
        num_w = 0
        for x in range(i, i+8):
            
            for y in range(j, j+8):
                if arr[x][y] != arr_b[x-i][y-j]:
                    num_b+=1
                if arr[x][y] != arr_w[x-i][y-j]:
                    num_w+=1
        result_b.append(num_b)
        result_w.append(num_w)
            
print(min(min(result_b),min(result_w)))