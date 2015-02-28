import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(';')
	l = line[0].split(',')
	k = int(line[1])
	result = []
	total = []
        count = 0	
	for i in l:
            count += 1
	    result.append(i)
	    if count%k == 0:
                total.extend(result[::-1])
		result = []
	    if count == len(l):
		total.extend(result)
	print ','.join(total)

test_cases.close()
