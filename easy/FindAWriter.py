import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split('|')
	author = line[0]
	key = [int(i) for i in line[1].split()]
        print ''.join(author[i-1] for i in key)
test_cases.close()
