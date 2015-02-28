import sys
from string import ascii_letters
from collections import Counter

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().lower()
	counter = Counter(line)
	alphabets = ascii_letters.split('A')[0]
	results = []
	for i in alphabets:
            if i not in counter.keys():
                results.append(i)
	if not results:
	    print "NULL"
	else:
	    print ''.join(results)
test_cases.close()
