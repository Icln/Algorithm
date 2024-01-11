P=int(input())
for _ in range(P):
    arr=list(map(int,input().split()))
    total=0
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)): 
            if arr[i] > arr[j]:  
                arr[i],arr[j] = arr[j],arr[i]  
                total+=1
    print(arr[0], total)