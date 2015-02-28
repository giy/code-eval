import sys
import pdb
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        nos = [int(i) for i in test.strip().split(',')]
        n, m = nos[0], nos[1]
        quotient = n/m
	remainder = abs(n - m*quotient)
	print remainder
test_cases.close()
