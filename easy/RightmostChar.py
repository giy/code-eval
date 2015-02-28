import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        inputs = test.strip().split(',')
        sentence = inputs[0]
	c = inputs[1]
	print sentence.rfind(c)
test_cases.close()
