#https://open.kattis.com/problems/whatdoesthefoxsay
import sys
import re

cases=int(input())

for _ in range(cases):
    #recording of sounds
    r = sys.stdin.readline()
    #List of all the sounds animals make
    for line in sys.stdin:
        if(line.rstrip()=="what does the fox say?"):
            break
        else:
            #split animal and sound (and rstrip to remove \n)
            sound=line.rstrip().split(" ")
            r=re.sub(r'\b'+sound[len(sound)-1]+r'\b',"",r)
    print(r) 