#https://open.kattis.com/problems/abc

#abc = list(map(int,input().split()))
#order=list(input())
#output=""

#c = max(abc)
#a = min(abc)

#for i in abc:
    #if i < c and i > a:
        #b=i

#def f(x):
   #return { 
        #"A": a,
        #"B": b,
        #"C": c,
   #}[x]

#for x in order:
    #output=output+str(f(x))+' '

#print(output)

#zip for at sammenholde 2 lister, map for at inputte argumenter til en funktion
#https://stackoverflow.com/questions/25468545/what-does-map-mean-in-python
#https://stackoverflow.com/questions/71762287/kattis-problem-abc-with-python3-works-fine-in-local-compiler-but-when-on-submi

order = dict(zip("ABC", sorted(input().split(), key=int)))
print(*map(order.get, input()),sep=" ")