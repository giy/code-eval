import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        no = int(test.strip())
	bin_no = bin(no)[2:]
	counter = Counter(bin_no)
	number_of_ones = counter.get('1')
	if number_of_ones:
	    print number_of_ones
	else:
            print 0
test_cases.close()
