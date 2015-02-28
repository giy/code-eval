import sys
import pdb

def permutations(line, n, str_a):
    if len(str_a) == n:
        print str_a
    else:
	for c in line:
	    if not c in str_a:
	        permutations(line, n, str_a + c)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = sorted(list(test.strip()))
    n = len(line)
    print permutations(line, n, "")

test_cases.close()
