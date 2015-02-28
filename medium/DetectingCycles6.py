import sys

def detectCycle(nos, i):
    cycleBeginsAt = i
    tortoise = 0
    hare = cycleBeginsAt
    for i in range(len(nos)):
	if nos[hare] == nos[tortoise]:
            break
        tortoise += 1
	hare = (hare + 1)%(len(nos))
    cycleBeginsAt = tortoise
    result = []
    for i in range(tortoise, len(nos)):
        if nos[i] not in result:
	    result.append(nos[i])
	else:
	    break
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
        if hare == tortoise:
            print ' '.join([str(x) for x in detectCycle(nos, i)])
	    break
test_cases.close()
