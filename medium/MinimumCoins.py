import sys
test_cases = open(sys.argv[1], 'r')

w = [1, 3, 5]

def minCoins(total):
    i = 0
    prev = w[0]
    while w[i] <= total:
        prev = w[i]
	i += 1
	if i == len(w):
	    break;
    total = total - prev
    result.append(prev)
    if total > 0:
        return minCoins(total)
    return result

for test in test_cases:
    if test:
        total = int(test.strip())
	result = []
	print len(minCoins(total))
test_cases.close()
