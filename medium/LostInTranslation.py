import sys
import string

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
	translation = string.maketrans('abcdefjvrkmnpqulwxyziostgh','yhesocuptilbrzjgfmaqdknwvx')
	print string.translate(line, translation)

test_cases.close()
