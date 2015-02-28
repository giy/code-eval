import sys
from collections import Counter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        nos = test.strip().split(',')
	x = [int(i) for i in nos]
	count = Counter(x)
	l = len(x)
	max = count.most_common()[0][0]
	max_l = count.most_common()[0][1]
        if 2*max_l > l:
	    print max
	else:
	    print "None"
test_cases.close()
