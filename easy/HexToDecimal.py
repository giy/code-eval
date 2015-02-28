import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        no = test.strip()
	print int(no, 16)
test_cases.close()
