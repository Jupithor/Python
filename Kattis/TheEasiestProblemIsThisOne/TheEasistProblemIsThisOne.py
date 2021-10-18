#https://open.kattis.com/problems/easiest

import sys
def findsum(n):
    if n == 0:
        return 0
    else:
        return (n%10+findsum(n//10))

for input in sys.stdin:
    n=int(input)
    if (n == 0):
        break
    sum=findsum(n)
    i=10
    msum=0
    while(sum!=msum):
        i+=1
        msum=findsum(n*i)
    print(i)
    