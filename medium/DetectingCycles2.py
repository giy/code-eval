import sys

def printCycle(x, tortoise):
    result = []
    hare = tortoise
    i = 0
    while 2*i < len(x):
        t = x[i]
        h = x[hare]
	if t == h and t not in result:
	    result.append(t)
	i += 1
    return ' '.join(result)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    l = test.strip().split()
    i = 0
    prev_hare = None
    while 2*i < len(l):
        tortoise = l[i]
	hare = l[2*i]
	if hare == prev_hare:
	    print hare
	    break
        if hare == tortoise and i != 0:
	    print printCycle(l, i)
	    break

	i += 1
	prev_hare = hare

test_cases.close()
