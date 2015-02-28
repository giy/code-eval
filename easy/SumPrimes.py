import sys
import pdb
def sumPrimes(n):
    l = 8000
    prime_nos = [True for i in range(0, limit)]
    prime_nos[0] = False
    prime_nos[1] = False
    pdb.set_trace()
    for i in xrange(1, int(l ** 0.5 + 1)):
        if primes[i]:


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        print sumPrimes(int(test))

test_cases.close()
