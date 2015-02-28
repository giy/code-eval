import sys

l = 41400
primes = [True for i in range(l)]
primes[0] = False
primes[1] = False

for i in range(1, int(l**0.5 + 1)):
    if primes[i]:
        for j in range(i*i, l, i):
	    primes[j] = False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x = int(test.strip())
    result = [str(i) for i in range(len(primes[:x])) if primes[i]]
    print ','.join(result)

test_cases.close()




