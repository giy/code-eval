import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split()
	no = line[0]
	pattern = line[1]
	add = True
        if pattern.find('+') > 0:
	    pos = pattern.find('+')
	else:
	    pos = pattern.find('-')
	    add = False
        f = int(no[:pos])
	s = int(no[pos:])
	if add:
	    print f + s
	else:
	    print f - s
test_cases.close()
