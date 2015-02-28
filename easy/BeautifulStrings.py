import sys
from string import ascii_letters
from collections import Counter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().lower()
        l = ''.join(i for i in line if i in ascii_letters)
        x = Counter(l)
        weight = 26
	total = 0
	for key,value in x.most_common():
	    total += value * weight
            weight -= 1
	print total
test_cases.close()
