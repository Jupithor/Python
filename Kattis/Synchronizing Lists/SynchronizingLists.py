#https://open.kattis.com/problems/synchronizinglists

import sys

n=1
while(n!=0):
    n=int(input())
    l1=[]
    l1o=[]
    l2=[]
    for _ in range(n):
        k=int(input())
        l1.append(k)
        l1o.append(k)
    for _ in range(n):
        l2.append(int(input()))
    l1.sort()
    l2.sort()
    m={}
    for _ in range(n):
        m[l1[_]]=l2[_]

    for _ in range(n):
        print(m.get(l1o[_]))
    print("\n")