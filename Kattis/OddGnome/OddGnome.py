#https://open.kattis.com/problems/oddgnome
import sys

cases = int(sys.stdin.readline())

for case in range(cases):
    temp = list(map(int, sys.stdin.readline().split()))
    gnomes = temp[0]

    for x in range(1,gnomes):
        low = temp[x]+1
        high = temp[x+1]
        if not low == high:
            print(x+1)
            break