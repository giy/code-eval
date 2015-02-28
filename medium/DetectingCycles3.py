import sys

def printCycle(x, tortoise):
    begin = 0
    result = []
    t = x[begin]
    h = x[tortoise]
    while t != h:
        begin += 1
	tortoise += 1
        t = x[begin]
	h = x[tortoise]
    result.append(x[begin])

    l = len(x)
    start = begin + 1
    while start < l:
        if x[start] not in result:
	    result.append(x[start])
	else:
	    break
        start += 1
    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    l = test.strip().split()
    i = 0
    prev_hare = None
    cycle = False
    while 2*i < len(l):
        tortoise = l[i]
	hare = l[2*i]
	if hare == prev_hare:
            print hare
	    cycle = True
	    break
        if hare == tortoise and i != 0:
	    print ' '.join(printCycle(l, i))
	    cycle = True
	    break
	i = i + 1
	prev_hare = hare
    if not cycle:
	print None

test_cases.close()
