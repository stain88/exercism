def is_pangram(phrase):
	alphabet = set("abcdefghijklmnopqrstuvwxyz")
	return not (alphabet - set(phrase.lower()))