#https://open.kattis.com/problems/lindenmayorsystem

import sys
import string

n,m = map(int, input().split())
#make map of each char
rules = {chr(64+i):chr(64+i) for i in range(1,27)}

#read all the rules into x and y and put into map
for _ in range(n):
    x,y = input().split(' -> ')
    rules[x] = y
seq = input()

#create the sequence
for _ in range(m):
    seq = ''.join((rules[s] for s in seq))
print(seq)