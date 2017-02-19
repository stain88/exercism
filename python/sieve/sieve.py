def sieve(input):
	primes = [None, None] + [True] * (input - 1)
	for p in range(2, input+1):
		if primes[p]:
			for m in range(2*p,input+1,p):
				primes[m] = None
	return [i for i, p in enumerate(primes) if p]

# def sieve(input):
# 	primes = range(2,input+1)
# 	for p in primes:
# 		primes = filter(lambda x: x==p or x % p != 0, primes)
# 	return primes