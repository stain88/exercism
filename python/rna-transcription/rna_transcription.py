def to_rna(dna):
	rna = ""
	for char in dna:
		if char not in ["C","G","T","A"]:
			return ''
		else:
			if char == "C":
				rna += "G"
			if char == "G":
				rna += "C"
			if char == "T":
				rna += "A"
			if char == "A":
				rna += "U"
	return rna