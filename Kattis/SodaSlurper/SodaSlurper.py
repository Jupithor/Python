#https://open.kattis.com/problems/sodaslurper

import sys

#e=empty bottles, f=found empty bottles, c=cost of new bottles
e,f,c = map(int,input().split())
e=e+f
d=0
#Recursive approach - e=empty bottles, d=drank bottles 
def drink(e, d):
    #exit recursion if we have less bottles then cost of a new bottles
    if(e<c):
        #return total number of drank bottles
        return d
    else:
        #New bottles we can buy
        b=e//c
        #Empty bottles left AFTER drinking the new bottles
        e=(e%c)+b
        #Updating total number of bottles drank
        d=d+b
        return drink(e,d)

print(drink(e,d))