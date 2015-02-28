import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        no = int(test.strip('\r\n'))
	sum = 0
        while no > 0:
	    dig = no % 10
	    no = no / 10
	    sum += dig
        print sum
test_cases.close()
