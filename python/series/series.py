import re

def slices(string, size):
	if size < 1 or size > len(string):
		raise ValueError
	matches = re.findall(r'(?=(\d{'+str(size)+'}))', string)
	return map(lambda m: map(int, (i for i in list(m))), matches)