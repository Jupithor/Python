#https://open.kattis.com/problems/volim

import sys

#k=(start) position of box, n=numbers of questions in the game, t=time passed, z=answer given
k=int(input())
n=int(input())
#Time before bomb goes off
time=210

for _ in range(n):
    t,z = input().split()
    t=int(t)
    time=time-t
    if(time<0):
        print(k)
        break
    if(z=='T'):
        k = 1 if (k==8) else k+1