import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        a = test.strip().split(';')
	line = a[0].split()
	indices = a[1].split()
	indices = [int(i) for i in indices]
	cor_len = len(indices) + 1
	missing = (cor_len * (cor_len + 1))/2 - sum(indices)
	x = zip(line, indices)
	x.append((line[-1], missing))
	x.sort(key = lambda t: t[1])
	result = ' '.join(t[0] for t in x)
	print result
test_cases.close()
