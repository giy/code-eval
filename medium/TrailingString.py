import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip().split(',')
	s = ''.join(test[0])
	sub_string = ''.join(test[1])
        l_sub_string = len(sub_string)
	l_s = len(s)
	if s[l_s - l_sub_string: l_s] == sub_string:
	    print 1
	else:
	    print 0
test_cases.close()
