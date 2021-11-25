#https://open.kattis.com/problems/kornislav

import sys

l= list(map(int,input().split()))
l.sort()
print(l[0]*l[-2])