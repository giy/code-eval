import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        w = test.strip('\n').split()
	first_word = w[0]
	l_f = len(first_word)
	longest_word = first_word
	for wd in w[1:]:
	    if len(wd) > l_f:
                l_f = len(wd)
		longest_word = wd
	print longest_word
test_cases.close()
