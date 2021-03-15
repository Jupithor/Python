#https://open.kattis.com/problems/speedlimit
import sys

for line in sys.stdin:
    n=int(line)
    if(n==-1):
        break
    s,t,accuHour,total=0,0,0,0

    for _ in range(n):
        accuHour = t
        s,t = map(int,input().split())
        total+=s*(t-accuHour)
    print(total, "miles")


