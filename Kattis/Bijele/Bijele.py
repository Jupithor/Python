#https://open.kattis.com/problems/bijele

import sys

CorrectPieces = [1,1,2,2,2,8]

#read input as list of ints
ActualPieces = list(map(int,sys.stdin.readline().split()))

for i in range(len(CorrectPieces)):
    print(CorrectPieces[i]-ActualPieces[i], end=" ")




