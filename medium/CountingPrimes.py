import sys

l = 8000
primes = [True for i in range(l)]
primes[0] = False
primes[1] = False

for i in range(1, int(l**0.5 + 1)):
    if primes[i]:
        for j in range(i*i, l, i):
	    primes[j] = False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nos = test.strip().split(',')
    to = int(nos[0])
    f = int(nos[1])
    total = 0
    for i in range(to, f+1):
        if primes[i]:
	    total += 1
    print total


