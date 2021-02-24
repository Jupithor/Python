#https://open.kattis.com/problems/boatparts

import sys

info = list(map(int, sys.stdin.readline().split()))
parts = info[0]
days = info[1]
items=[]
replaced=[]

#read all lines
for line in sys.stdin.readlines():
        items.append(line)

for day in range(days):
   #Check if item is already replaced
   if not items[day] in replaced:
       replaced.append(items[day])
       #print days if total number of parts has been replaced
       if len(replaced) == parts:
           print(day+1)
           sys.exit()
print("paradox avoided")

    

    

