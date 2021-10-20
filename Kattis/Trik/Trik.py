#https://open.kattis.com/problems/trik

import sys

cup=1
moves = sys.stdin.readline()

for c in moves:
    if (c=='A' and cup != 3):
        cup = 3 - cup
    if (c=='B' and cup != 1):
        cup = 5 - cup
    if (c=='C' and cup != 2):
        cup = 4 - cup

print(cup)