#https://open.kattis.com/problems/batterup
import sys

ATBats = sys.stdin.readline()
Bat = map(int, sys.stdin.readline().split())
valid = int()
bases = int()
for x in Bat:
    if x != -1:
        valid+=1
        bases+=x

print(bases/valid)

