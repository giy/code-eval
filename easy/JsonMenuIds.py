import sys
import json
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        sum = 0
	s = test.strip()
	dict = json.loads(s)
        items = dict['menu']['items']
	for elem in items:
	    if elem and 'label' in elem:
                sum += elem['id']
	print sum
test_cases.close()
