def detect_anagrams(matcher, matches):
	return filter(lambda m: matcher.lower() != m.lower() and ''.join(sorted(matcher.lower())) == ''.join(sorted(m.lower())), matches)