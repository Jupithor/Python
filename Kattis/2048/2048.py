#https://open.kattis.com/problems/2048

input_matrix = []

#get the matrix
#for i in range(4):
    #row = input().split(' ')
    #input_matrix.append(row)

#0-left,1-up,2-right,3-down
#move=int(input())

test_input =  [[2, 0, 0, 2], \
[4, 16, 8 ,2], \
[2, 64, 32, 4], \
[1024, 1024, 64, 0]]\


def move_left(numbers):
    n = []
    new_numbers = []
    for number in numbers:
        if number != 0:
            n.append(number)
    i = 0
    while i < len(n):
        if i < len(n)-1 and n[i] == n[i+1]:
            new_numbers.append(n[i]*2)
            i += 2
        else:
            new_numbers.append(n[i])
            i += 1
    while len(new_numbers) != 4:
        new_numbers.append(0)
    return new_numbers

move_left(test_input)