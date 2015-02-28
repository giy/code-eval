import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(',')
	no = int(line[0])
	a = int(line[1])
	b = int(line[2])
        bin_no = '{0:b}'.format(no)
	l = len(bin_no)
	ans =  bin_no[l-a] == bin_no[l-b]
	print str(ans).lower()
test_cases.close()
