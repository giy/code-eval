import sys
import textwrap

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
	print '\n'.join(textwrap.wrap(line, 80))
test_cases.close()
