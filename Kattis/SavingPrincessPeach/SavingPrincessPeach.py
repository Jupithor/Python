#https://open.kattis.com/problems/princesspeach

import sys

n,y = map(int, input().split())

obstacles = set([])

for obs in range(y):
    obstacles.add(int(input()))

for _ in range(n):
    if not _ in obstacles:
        print(_)

print("Mario got",len(obstacles),"of the dangerous obstacles.")