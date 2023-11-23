from collections import deque
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)
result = 0

while True:
    result += 1

    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(n - 2, -1, -1):
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            belt[i + 1] -= 1
            robot[i + 1] = 1
            robot[i] = 0
    robot[-1] = 0

    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= k:
        break
print(result)
