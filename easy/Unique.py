import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        l = test.strip().split(',')
        s = list(sorted(set(int(i) for i in l)))
	print ','.join((str(j) for j in s))
test_cases.close()
