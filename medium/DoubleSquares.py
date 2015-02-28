import sys
import math

def doubleSquares(no):
    sqrt = int(math.sqrt(no))
    result = []
    count = 0
    for i in range(sqrt + 1):
	y = int((no - (i**2))**0.5)
	if i > y:
           break
        if (i**2 + y**2) == no:
            count += 1
    return count

test_cases = open(sys.argv[1], 'r')
c = 0
for test in test_cases:
    c += 1 
    if c == 1:
        continue
    no = int(test.strip())
    if no == 0:
        print 1
        continue
    print doubleSquares(no)
test_cases.close()
