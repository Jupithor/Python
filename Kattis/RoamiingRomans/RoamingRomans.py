#https://open.kattis.com/problems/romans

eMile = float(input())

convert = 1000*(5280/4854)

ans = round(eMile*convert)

print(ans)