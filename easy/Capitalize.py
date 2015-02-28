import sys
def toUpperCase(line):
    wds = line.split()
    return ' '.join(w[0].upper() + w[1:] for w in wds)

test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    if line:
        print toUpperCase(line.strip())

test_cases.close()
