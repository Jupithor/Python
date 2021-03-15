#https://open.kattis.com/problems/spavanac

hr, min = map(int, input().split())

min-=45

if(min<0):
    min+=60
    hr-=1
if(hr<0):
    hr=23
print(hr, min)