import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split()
	print line[-2]
test_cases.close()
