from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    time = 0
    cur = 0
    
    while truck:
        time += 1
        cur -= bridge.popleft()
        
        if cur + truck[0] <= weight:
            cur += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
            
    return time + bridge_length

