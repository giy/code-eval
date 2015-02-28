import sys
from string import ascii_letters
s = 'abcdefghij'
d = {}
c = 0
for k in s:
    d[k] = c
    c += 1
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
	x = []
	for i in line:
	    if i.isdigit():
	        x.append(i)
	    elif i in d:
                x.append(str(d[i]))
	l = ''.join(x)
	if len(l) == 0:
	    print 'NONE'
        else:
	    print l
test_cases.close()
