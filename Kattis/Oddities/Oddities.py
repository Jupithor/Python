#https://open.kattis.com/problems/oddities

cases = int(input())

for case in range(cases):
    n = int(input())
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n, "is odd")