import sys
from string import ascii_letters
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
	upper = True
	l = []
	for i in line:
	    l.append(i.upper() if upper and i in ascii_letters else i)
	    if i in ascii_letters:
                 upper = not upper
        print ''.join(l)
test_cases.close()
