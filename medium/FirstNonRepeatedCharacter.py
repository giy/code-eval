import sys
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        counter = Counter(test.strip())
	for c in test.strip():
	    if counter[c] == 1:
	        print c
		break
test_cases.close()
