import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	print ' '.join(test.split()[::-1])
test_cases.close()
