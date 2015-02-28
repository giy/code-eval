import sys
import pdb

def josephus(x, m):
    m = m - 1
    i = m
    result = []
    while len(x) > 1:
        result.append(x.pop(i))  # 0 1 3 4 5 3 took 2s place so only count 2 more to 5, since list is popped
        i = (i + m)%len(x)
    result.append(x[0])
    return [str(x) for x in result]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(',')
	no = int(line[0])
	x = range(no)
	m = int(line[1])
        print ' '.join(josephus(x, m))

test_cases.close()
