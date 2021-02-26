#https://open.kattis.com/problems/nastyhacks

cases = int(input())

for case in range(cases):
    r,e,c = map(int,input().split())
    if r < (e-c):
        print("advertise")
    elif r == (e-c):
        print("does not matter")
    else:
        print("do not advertise")