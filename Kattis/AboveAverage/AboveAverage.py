#https://open.kattis.com/problems/aboveaverage

c = int(input())

for i in range(c):
    case=list(map(int,input().split()))
    n=case.pop(0)
    avg=sum(case)/len(case)
    aboveAvg=0
    for i in case:
        if i>avg:
            aboveAvg+=1
    percentAboveAvg=aboveAvg/len(case)
    print("{:.3%}".format(percentAboveAvg))
