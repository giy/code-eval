import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	l = []
        line = test.strip().split()
        for word in line:
	    # range(len('cat')-1) = [0,1] .. range(3) = [0,1,2] go until one letter before the end
	    l.append(''.join([word[i] for i in range(len(word)-1) if word[i] != word[i+1]] + [word[-1]]))
	print ' '.join(l)
test_cases.close()

