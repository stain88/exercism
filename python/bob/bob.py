import re

def hey(what):
	if re.match(r'^\s+$', what) or what == "":
		return 'Fine. Be that way!'
	if what == what.upper() and not re.match(r'^[\d, \?]+$', what):
		return 'Whoa, chill out!'
	if what.strip()[-1:] == '?':
		return 'Sure.'
	return 'Whatever.'
