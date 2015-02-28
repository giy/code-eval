import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        try:
	    no = int(test.strip())
	    print "{0:b}".format(no)
	except ValueError:
	    pass
test_cases.close()
