import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        s = test.strip().split()
        number = s[0]
	count = 0
	result = []
        for i in s:
            if i == number:
                count += 1
            else:
                result.append('{0} {1}'.format(count, number))
                number, count = i, 1

        result.append('{0} {1}'.format(count, number))
        print ' '.join(result)          
test_cases.close()
