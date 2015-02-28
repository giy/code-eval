import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip('\r\n').split(';')
        first = line[0].split(',')
	second = line[1].split(',')	
        inter = set(first) & set(second)
	print ','.join(sorted(inter))
test_cases.close()
