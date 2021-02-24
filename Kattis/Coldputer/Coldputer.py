#https://open.kattis.com/problems/cold

import sys

days = int(sys.stdin.readline())
temps = list(map(int,sys.stdin.readline().split()))

count=0

for day in range(days):
    if temps[day] < 0:
        count+=1

print(count)
