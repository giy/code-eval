import sys
import math
import pdb

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.strip().split(';')
    dim = int(line[0])
    n = dim
    nos = [int(i) for i in line[1].strip().split(',')]
    matrix = []
    result = []
    for i in range(0, len(nos)):
	result.append(nos[i])
	if (i+1)%n == 0:
	    matrix.append(result)
	    result = []
            result.append(nos[i])
    h = (range(i, i + dim, 1) for i in xrange(0, dim ** 2, dim))
    v = (range(i, dim ** 2, dim) for i in xrange(0, dim))
    check_horiz = all(len({nos[j] for j in i}) == dim for i in h)
    check_verti = all(len({nos[j] for j in i}) == dim for i in v)
    print check_horiz and check_verti

test_cases.close()
