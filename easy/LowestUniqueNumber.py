import sys
from collections import Counter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        l = [int(i) for i in test.strip().split()]
	c_lcom = Counter(l)
	min = 10
	for k, v in c_lcom.items():
	    if v == 1:
		if k < min:
		    min = k
        if min != 10:
	    print l.index(min) + 1
	else:
	    print 0
test_cases.close()
