#https://open.kattis.com/problems/3dprinter

import sys
import math
n=int(input())

days=1+math.ceil(math.log(n)/math.log(2))
print(days)