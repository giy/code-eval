import sys
import re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip(' \n')
	if len(line) <= 55:
	    print line
        elif len(line) > 55:
	    line = line[:40]
	    if line.rfind(' ') != -1: line = line[0:line.rfind(' ')]
            print line + '... <Read More>'
test_cases.close()
