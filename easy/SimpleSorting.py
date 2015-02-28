import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        s = test.strip().split()
	l = [float(i) for i in s]
        sort_l = sorted(l)
	f_l = ['{:.3f}'.format(i) for i in sort_l]
	print ' '.join(str(i) for i in f_l)
test_cases.close()
