import sys
def calc_fib(n):
    # Since the first and second numbers are 0 and 1, go till n-2
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    else:
	f = 0
	s = 1
        for i in range(0, n - 1):
            t = f + s
	    f = s
	    s = t
        return t

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        nth = int(test.strip('\n'))
	print calc_fib(nth)
test_cases.close()
