import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        inputs = test.strip().split(',')
	s = inputs[0].strip()
	to_remove = inputs[1].strip()
	print ''.join(i for i in s if i not in to_remove)
test_cases.close()
