#https://open.kattis.com/problems/savingforretirement

B, retB, savB, A, savA = map(int, input().split())

amountB = (retB-B)*savB

retA = int(amountB/savA)

print(retA+A+1)

