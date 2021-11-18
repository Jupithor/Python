#https://open.kattis.com/problems/pyramids

import sys

n=int(input())
i=1
h=0
while(n>=0):
    b=i*i
    n=n-b
    if(n>=0):
        h=h+1
        i=i+2
print(h)
