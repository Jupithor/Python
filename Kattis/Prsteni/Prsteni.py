#https://open.kattis.com/problems/prsteni

import sys
from fractions import Fraction

n=int(input())
r=list(map(int,input().split()))
a=1
for i in range(0,len(r)-1):
    if(i!=len(r)-1):
        a=Fraction(r[i]*a,r[i+1])
        if((float(a)).is_integer()):
            print(str(a)+"/1")
        else:
            print(a)