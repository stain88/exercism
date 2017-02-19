def sieve(input):
	primes = range(2,input+1)
	for p in primes:
		primes = filter(lambda x: x==p or x % p != 0, primes)
	return primes
