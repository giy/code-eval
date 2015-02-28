import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip('\n')
	if len(line) <= 55:
	    print line
        elif len(line) > 55:
	    words = line.strip().split()
	    l = line[0:39].strip()
	    last = l.split()[-1]
	    if last not in words:
	        print line[0:39 - (len(last))].strip() + "... <Read More>"
	    else:
		print l[0:39] + "... <Read More>"
test_cases.close()
