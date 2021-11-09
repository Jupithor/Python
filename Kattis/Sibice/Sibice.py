#https://open.kattis.com/problems/sibice

import sys
import math


n,w,h=map(int,input().split())
d=int(math.sqrt(w**2+h**2))
for line in sys.stdin:
    stick=int(line)
    if stick <= max(d,w,h):
        print("DA")
    else:
        print("NE")