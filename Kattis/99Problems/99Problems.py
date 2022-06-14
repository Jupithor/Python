#https://open.kattis.com/problems/99problems

#import sys
#import math
#n = input()

#if int(n)<149:
    #print(99)
    #quit()
#if (int(n[-2:])<49):
    #print(str(int(n[:-2])-1)+str(99))
#else:
    #print(int(n[:-2]+str(99)))

#below is a much better solution:)
n=int(input())
if n < 100:
    print(99)
    quit()
#to make sure 249 gets converted to 299
n+=1.1
#Divide by 100 to 'exclude' the last two digits and then round it to go either down or up
r=round(n/100)
#Get last two digits back
k=r*100
#subtract 1 to get 99
print(k-1)