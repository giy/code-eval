import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        sentence = test.strip()
	print sentence.swapcase()
test_cases.close()
