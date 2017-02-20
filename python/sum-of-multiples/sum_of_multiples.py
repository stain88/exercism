def sum_of_multiples(limit, factors):
	multiples = filter(lambda x: is_multiple(x, factors), range(1,limit))
	return reduce((lambda x, y: x + y), multiples, 0)

def is_multiple(n, factors):
	for f in factors:
		if f != 0:
			if n % f == 0:
				return True
	return False