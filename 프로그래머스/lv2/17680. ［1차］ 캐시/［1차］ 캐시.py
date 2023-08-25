from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque() 
    cities = [i.upper() for i in cities]
    cache.append(cities[0])
    result = 5
    
    for i in range(2, len(cities) + 1):
        if cities[i - 1] not in cache:
            result += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(cities[i - 1])            
        else:
            result += 1
            cache.remove(cities[i - 1])
            cache.append(cities[i - 1])
    return result