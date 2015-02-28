import sys
from collections import Counter

def followingInteger(no):
    a = Counter(str(no))
    for i in xrange(no+1,1000000,1):
        b = Counter(str(i))
	if a == b:
            break
        x = sorted(a.items())
	y = sorted(b.items())
	if y[0][0] == '0':
            if x == y[1:] and a['0'] + 1 == b['0']: 
                break
	if x[0][0] == '0' and y[0][0] == '0':
            if x[1:] == y[1:] and a['0'] + 1 == b['0']:
                break
    return i


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
	print followingInteger(int(line))
test_cases.close()
