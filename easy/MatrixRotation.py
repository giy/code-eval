import sys
from itertools import chain
def to_matrix(x, each_row):
    return [x[i:i+each_row] for i in xrange(0, len(x), each_row)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        x = test.strip().split()
	no = len(x)
	each_row = int(no**0.5)
        mat = to_matrix(x, each_row)
	rot = zip(*mat[::-1])
	print ' '.join(list(chain.from_iterable(rot)))

test_cases.close()
