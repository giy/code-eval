limit = 1000

primes = [True for i in range(0, limit)]
primes[0] = False
primes[1] = False

# From 1 to sqrt(8000)
for i in range(1, int(limit ** 0.5 + 1)):
    if primes[i] == True:
        for j in range(i ** 2, limit, i):
	    primes[j] = False

largest = 0
for i in range(0, len(primes)-1):
    if primes[i] == True:
	if str(i) == str(i)[::-1]:
	   largest = i

print largest
