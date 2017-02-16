from itertools import groupby
import re

def encode(uncomp_string):
	compressed = ""
	for k, g in groupby(uncomp_string):
		num = len(list(g))
		compressed = compressed + str(num) + k if num > 1 else compressed + k
	return compressed


def decode(comp_string):
	decompressed = ""
	matches = re.findall(r'((\d*)([\W]|[A-z]))', comp_string)
	for m in matches:
		decompressed = decompressed + m[2] * int(m[1]) if m[1] else decompressed + m[2]
	return decompressed