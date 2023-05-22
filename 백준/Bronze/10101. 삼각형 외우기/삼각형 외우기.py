import sys
input = sys.stdin.readline
x = int(input())
y = int(input())
z = int(input())
if x == y and y == z and z == 60:
    print("Equilateral")
elif x+y+z != 180:
    print("Error")
elif x+y+z == 180 and x != y and y!=z and x != z:
    print("Scalene")
elif x+y+z == 180 and (x==y or y==z or z== x):
    print("Isosceles") 