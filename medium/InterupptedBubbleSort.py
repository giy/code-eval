import sys

def interruptedBubbleSort(x, n):
    n = min(n, len(x))
    while n > 0:
	n -= 1
        for i in xrange(1, len(x)):
	    if x[i-1] > x[i]:
	        temp = x[i]
		x[i] = x[i-1]
		x[i-1] = temp    
    return x

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.strip().split(' | ')
    x = [int(i) for i in line[0].split()]
    if len(x) == 0: continue
    n = int(line[1])
    print ' '.join([str(i) for i in interruptedBubbleSort(x, n)])

test_cases.close()
