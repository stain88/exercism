def distance(first, second):
	if len(first) != len(second):
		raise ValueError
	if first == second:
		return 0
	ham_value = 0
	for idx, c in enumerate(first):
		if c != second[idx]:
			ham_value += 1
	return ham_value