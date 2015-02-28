import sys

def sumOfIntegers(nos):
    total = 0
    max_total = 0
    for i in nos:
        total += i
	if total < 0:
	    total = 0
	if (total > max_total):
	    max_total = total
    return max_total

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(',')
	nos = [int(i) for i in line]
	x = max(nos)
	if x < 0:
	    print x
	else:
            print sumOfIntegers(nos)
test_cases.close()
