#https://open.kattis.com/problems/estimatingtheareaofacircle

import sys
import math

for line in sys.stdin.readlines():
    r,m,c=map(float,line.strip().split())
    if (r!=0 and m!=0 and c!=0):
        #real area
        a=math.pow(r,2)*math.pi
        #Estimate area
        e=4*(c/m)*r**2

        print(a,e)