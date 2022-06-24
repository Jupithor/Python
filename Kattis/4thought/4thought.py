#https://open.kattis.com/problems/4thought
import itertools

n=int(input())
vals = [4,4,4,4]
operators = ['+', '*', '-', '//']
perm={}

#makes cartesian product of the operatos
mut=[x for x in  itertools.product(operators, repeat=3)]

#for each of them we will add the vals in between
for x in mut:
    ops=''
    for (j, i) in zip(x,vals):
        #adding value in between
        ops=ops+str(i)+' '+str(j)+' '

    #adding the last value
    ops=ops+str(vals[-1])
    perm[eval(ops)]='{} = {}'.format(ops.replace('//','/'),eval(ops))

for i in range(n):
    k=int(input())
    if perm.get(k):
        print(perm.get(k))
    else:
        print("no solution")