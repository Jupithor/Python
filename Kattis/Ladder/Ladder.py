#https://open.kattis.com/problems/ladder

import sys
import math

h,v = map(int,(input().split()))
#sin(v) = katete/hyptenuse
#hyptenuse=Katete/sin(v) - remeber radians
hyp=math.ceil(h/math.sin(math.radians(v)))
print(hyp)
