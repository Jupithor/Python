#https://open.kattis.com/problems/sevenwonders

cards = input()

t = cards.count('T')
c = cards.count('C')
g = cards.count('G')

result = (t ** 2) + (c ** 2) + (g ** 2)

while (t > 0 and  c  > 0 and g > 0):
    result+=7
    t-=1
    c-=1
    g-=1

print(result)