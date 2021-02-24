#https://open.kattis.com/problems/cetvrta
import sys
from collections import Counter

coords = [[],[]]

#split input into x,y coordinats
for input in sys.stdin:
    x,y = map(int,input.split())
    coords[0].append(x)
    coords[1].append(y)

#find unique coord (the coordinate for the last point)
for coord in coords:
    freq = Counter(coord)
    for x in freq:
        if (freq[x] == 1):
            print(x, end=" ")