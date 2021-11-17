#https://open.kattis.com/problems/pet

import sys

i=1
Scoremap={}
for i in range(1,6):
    nrs=list(map(int,input().split()))
    nrs=sum(nrs)
    Scoremap[i]=nrs

max=max(Scoremap,key=Scoremap.get)
print(max, Scoremap.get(max))