import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    sequence = test.split()
    b = ''
    for i in xrange(0, len(sequence), 2):
        b += len(sequence[i + 1]) * ('0' if sequence[i] == '0' else '1')
    print int(b, 2)
