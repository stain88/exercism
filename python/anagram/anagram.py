def detect_anagrams(matcher, matches):
	return filter(lambda m: matcher.lower() != m.lower() and sorted(matcher.lower()) == sorted(m.lower()), matches)