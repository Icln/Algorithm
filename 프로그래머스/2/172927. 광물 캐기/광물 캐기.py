from collections import defaultdict
def solution(picks, minerals):
    minerals = minerals[: sum(picks) * 5] 
    
    answer = 0
    
    cnt = defaultdict(int)
    tired = defaultdict(list)
    tired[0], tired[1], tired[2] = [1, 1, 1], [5, 1, 1], [25, 5, 1]


    arr = []
    for i in range(len(minerals)):
        cnt[minerals[i]] += 1
        if (i + 1) % 5 == 0 or i == len(minerals) - 1:
            arr.append([cnt["diamond"], cnt["iron"], cnt["stone"]])
            cnt = defaultdict(int)

    arr.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)
    
    for d, i, s in arr:
        for j in range(3):
            if picks[j]:
                answer += d * tired[j][0] + i * tired[j][1] + s * tired[j][2]
                picks[j] -= 1
                break
                
    return answer