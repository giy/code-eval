import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    inputs = test.strip()
    mthToLast_index = int(inputs.split()[-1])
    x = inputs.split()[:-1]
    try:
	print x[-mthToLast_index]
    except IndexError:
	pass

test_cases.close()
