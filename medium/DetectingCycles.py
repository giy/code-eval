import sys

def detectCycle(nos, i):
    begin_t = 0
    begin_h = i
    while (nos[begin_t] != nos[begin_h]):
        begin_t += 1
	begin_h = (begin_h + 1)%(len(nos))
    cycle_begins_at = begin_t
    i = cycle_begins_at
    result = []
    while nos[i] not in result:
        result.append(nos[i])
	i += 1
    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nos = [int(i) for i in test.strip().split()]
    if len(nos) == 1:
        print nos[0]
	continue
    for i in range(1, len(nos)):
	tortoise = nos[i]
	hare = nos[(2*i)%len(nos)]
	if tortoise == hare:
	    cycle = detectCycle(nos, i)
	    print  ' '.join(str(x) for x in cycle)
            break

test_cases.close()
