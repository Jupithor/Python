#https://open.kattis.com/problems/simon
import sys
cases = int(input())

for line in sys.stdin:
    if line.startswith("simon says "):
        out = line.replace("simon says ","",1)
        print(out)
    else:
        print()
