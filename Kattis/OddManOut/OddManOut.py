#https://open.kattis.com/problems/oddmanout,
import sys
from collections import Counter

cases = int(input())

for case in range(cases):
    guests = int(input())
    invites = list(map(int, input().split()))
    freq = Counter(invites)
    for code in freq:
        if freq[code] == 1:
            print("Case #",case+1,": ",code, sep='')
            