#https://open.kattis.com/problems/fodelsedagsmemorisering

import sys

n=int(input())
birthdays=dict({})

for line in sys.stdin:
    s,c,d = line.split()
    c=int(c)
    if(d in birthdays):
        #get exisiting friends score
        temp=birthdays.get(d)[1]
        if temp < c:
            birthdays.update({d:[s,c]})
    else:
        birthdays[d]=[s,c]
#Nr of birthdays to remember
print(len(birthdays))
#names
names=[]
for name in birthdays.values():
    names.append(name[0])
names=sorted(names)
print(*names, sep='\n')