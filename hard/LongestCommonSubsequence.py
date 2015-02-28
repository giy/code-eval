import sys

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
	for j, y in enumerate(b):
	    if x == y:
	        lengths[i + 1][j + 1] = lengths[i][j] + 1
	    else:
		lengths[i + 1][j + 1] = max(lengths[i][j + 1], lengths[i + 1][j])
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
	if lengths[x][y] == lengths[x - 1][y]:
	    x = x - 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y = y - 1
	else:
	    #assert a[x - 1] == b[y - 1]
	    result = a[x - 1] + result
            x = x - 1
	    y = y - 1
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(';')
	a = line[0]
	b = line[1]
	print lcs(a, b)
test_cases.close()
