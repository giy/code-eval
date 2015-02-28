import sys

def calcPos(nos):
    l = len(nos)
    return range(1, l)

def calcDiffs(nos):
    result = []
    for i in range(1, len(nos)):
	diff = nos[i-1] - nos[i]
        result.append(abs(diff))
    return sorted(result)

def isJollyJumper(nos):
    pos = calcPos(nos)
    diffs = calcDiffs(nos)
    if pos == diffs:
	return 'Jolly'
    else:
	return 'Not jolly'

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nos = [int(i) for i in test.strip().split()]
    nos.pop(0)
    print isJollyJumper(nos)

test_cases.close()
