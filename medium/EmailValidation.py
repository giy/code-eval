import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
        patternString = "^[_A-Za-z0-9-\\.\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$|" + "^\"[_A-Za-z0-9-\\.\\+@]+(\\.[_A-Za-z0-9-]+)*\"@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
        #m = re.search(r'[\w._]+@\w+.\w+',line)
        m = re.search(patternString, line)
	if m:
	    print "true"
	else:
	    print "false"
test_cases.close()
