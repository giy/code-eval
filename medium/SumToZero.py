import sys
from itertools import combinations

def sumToZero(l):
    x = combinations(l, 4)
    c = 0
    for i in x:
	if sum(i) == 0:
	    c += 1
    return c

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(',')
	l = [int(i) for i in line]
	print sumToZero(l)
test_cases.close()
