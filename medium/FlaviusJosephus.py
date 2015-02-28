import sys

def josephus(x, m):
    result = []
    m = m-1
    i = m
    while len(x) > 1:
       result.append(x.pop(i))
       # [0, 1, 3, 4, 6, 7, 9] when you remove 8, 9 comes to the position of 9, i = 6, len(x) = 7 6+2%7 = 1 2 5 8 1
       i = (i + m) % len(x)
    result.append(x[0])
    result = [str(i) for i in result]
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(',')
	no = int(line[0])
	x = range(no)
	m = int(line[1])
        print ' '.join(josephus(x, m))

test_cases.close()
