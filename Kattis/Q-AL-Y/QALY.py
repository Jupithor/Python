#https://open.kattis.com/problems/qaly
cases = int(input())
QALY=0
for case in range(cases):
    # q = quality of life, y=number of years
    q,y = map(float, input().split())
    QALY += q*y

print(QALY)
