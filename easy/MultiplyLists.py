import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        lists = test.strip('\n').split('|')
	first = [int(a) for a in lists[0].split()]
	second = [int(b) for b in lists[1].split()]
	third = [(x * y) for x,y in zip(first,second)]
	t = [str(i) for i in third]
        print ' '.join(t)
test_cases.close()
