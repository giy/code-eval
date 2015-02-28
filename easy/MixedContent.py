import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	ints = []
	s = []
        line = test.strip().split(',')
	for i in line:
	    try:
	        d = int(i)
		ints.append(i)
	    except ValueError as e:
		 s.append(i)
    s_f = ','.join(s)
    i_f = ','.join(ints)
    if not i_f:
        print s_f
    elif not s_f:
	print i_f
    elif i_f and s_f:
	print s_f + "|" + i_f

test_cases.close()
