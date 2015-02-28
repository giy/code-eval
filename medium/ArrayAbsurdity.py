import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip().split(';')
	len = test[0]
	x = [int(i) for i in test[1].split(',')]
	counter = Counter(x)
	print counter.most_common()[0][0]
test_cases.close()
