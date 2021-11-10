#https://open.kattis.com/problems/modulo

import sys
numbers=set(())
for line in sys.stdin.readlines():
    nr=int(line)%42
    numbers.add(nr)
print(len(numbers))
