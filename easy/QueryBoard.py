import sys
import pdb

matrix = [[0 for i in xrange(2)] for j in xrange(2)]

def setCol(col, value):
    for row in matrix:
        row[col] = value

def setRow(row, value):
    matrix[row] = matrix[row] = [value for i in matrix[row]]

def queryRow(matrix, val):
    print sum(matrix[val])

def queryCol(matrix, val):
    print sum(row[val] for row in matrix)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        inputs = test.strip().split()
	operation = inputs[0]
	if operation == 'SetCol':
	    setCol(int(inputs[1]), int(inputs[2]))
	if operation == 'SetRow':
	    setRow(int(inputs[1]), int(inputs[2]))
        if operation == 'QueryRow':
            queryRow(int(inputs[1]))
	if operation == 'QueryCol':
            queryCol(int(inputs[1]))
        print matrix
test_cases.close()
