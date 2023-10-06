import copy
result = []
def dfs(idx, ticket, visit, tickets, airport):
    if len(airport) == len(tickets):
        airport.append(ticket[1])
        result.append(copy.deepcopy(airport))
        return
    
    for i, city in enumerate(tickets):
        if city[0] == ticket[1] and not visit[i]:
            visit[idx] = True     
            airport.append(city[0])
            dfs(i, city, visit, tickets, airport)
            airport.pop()
            visit[idx] = False
    
    return 
def solution(tickets):
    tickets.sort(key = lambda x:(x[0], x[1]))
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            airport = ["ICN"]
            visit = [False] * len(tickets)
            dfs(idx, ticket, visit, tickets, airport)
    return result[0]