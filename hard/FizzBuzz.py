import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.split()
        first_no = int(line[0])
        second_no = int(line[1])
        no_of_elements = int(line[-1])
        for count,i in enumerate(range(1, no_of_elements + 1)):
	    if i % first_no == 0 and i % second_no == 0: 
	        print 'FB', 
	    elif i % first_no == 0:
	        print 'F',
	    elif i % second_no == 0:
	        print 'B',
	    else:
		print str(i),
	    if count == (no_of_elements - 1):
	        print
test_cases.close()
