import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	cities = test.strip()[:len(test)-2].split('; ')
	d = []
        for x in cities:
	    dis = x.split(',')[1]
	    d.append(int(dis))
	s_d = sorted(d)
	result = []
	result.append(s_d[0])
	for i in range(1, len(s_d)):
	    result.append(s_d[i] - s_d[i-1])
	print ','.join([str(i) for i in result])
test_cases.close()
