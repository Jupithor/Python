#https://open.kattis.com/problems/reverserot

import sys

for line in sys.stdin:
    s = list(line.split())
    n = int(s[0])
    if n == 0:
        sys.exit()
    reverse = s[1][::-1]

    for c in reverse:
        #change _ to z+1
        if(ord(c) == 95):
            c = chr(91)
        #change . to z+2
        elif(ord(c) == 46):
            c = chr(92)

        c = chr( (ord(c)- 65 + n) % 28 + 65 )

        #change z+1 to _
        if(ord(c) == 91):
            c = chr(95)
        #change z+2 to .
        elif(ord(c) == 92):
            c = chr(46)

        print(c, end='')
    print()
   