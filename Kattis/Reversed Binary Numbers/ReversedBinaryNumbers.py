#https://open.kattis.com/problems/reversebinary

import sys

n=int(input())
tobinary="{0:b}".format(n)
revb=tobinary[::-1]
nrev=int(revb,2)
print(nrev)
