#https://open.kattis.com/problems/acm

#q=question,a=answer(right/wrong),t=time

d={}
score=0
count=0

entry=input()

while entry != "-1": 
    t,q,a = entry.split()
    if q in d:
        if (d[q][0] == "wrong" and a == "wrong"):
            d[q][1] = d[q][1]+20
        if (d[q][0] == "wrong" and a == "right"):
            d[q][1] = d[q][1]+int(t)
            d[q][0] = a
    else:
        if a == "wrong":
            d[q]=[a,+20]
        else:
            d[q]=[a,int(t)]
    entry=input()

for k,v in d.items():
    if v[0]=="right":
        score+=v[1]
        count+=1

print(count,score)