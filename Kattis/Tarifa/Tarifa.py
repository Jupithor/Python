#https://open.kattis.com/problems/tarifa

import sys

data=int(input())
monts=int(input())
output=data
for line in sys.stdin:
    output+=data-int(line)
print(output)