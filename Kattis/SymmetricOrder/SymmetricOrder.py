#https://open.kattis.com/problems/symmetricorder

import sys
sets = 1
for line in sys.stdin:
    n = int(line)
    if (n==0):
        break
    print("SET", sets)
    #initialise list
    names = [0]*n
    #put input names in opposit places in the list
    for _ in range(n//2):
        names[_] = input()
        names[n-_-1]=input()
    #if the list is uneven, there will be a missing name in the middle
    if(n%2 != 0):
        names[n//2] = input()
    print(*names, sep="\n")
    sets+=1