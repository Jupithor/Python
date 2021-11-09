#https://open.kattis.com/problems/smil
import sys
smils=[':)',';)',':-)',';-)']

symbols=input()

for _ in range (len(symbols)):
    if symbols[_:_+2] in smils or symbols[_:_+3] in smils:
        print(_)