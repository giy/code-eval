limit = 8000

primes = [True for i in xrange(0, limit)]
primes[0] = False
primes[1] = False
#0 and 1 are not prime numbers

for i in range(1, int(limit ** 0.5 + 1)):
    if primes[i] == True:
        for j in xrange(i**2, limit, i):
	    primes[j] = False

num_primes = 1000

i = 0
total_sum = 0
while num_primes:
    if primes[i] == True:
        total_sum += i
	num_primes -= 1
    i += 1

print total_sum
