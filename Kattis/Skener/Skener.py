#https://open.kattis.com/problems/skener

r,c,zr,zc = map(int,input().split())

for i in range(r):
    line=list(input())
    for j in range(zr):
        for k in line:
            print(zc*k, end='', flush=True)
        print('\r')