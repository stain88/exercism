alphabet = "abcdefghijklmnopqrstuvwxyz"

def inverse_letter(letter):
	if letter.isdigit():
		return letter
	try:
		return alphabet[25-alphabet.index(letter)]
	except:
		return None

def decode(encoded):
	return ''.join(map(lambda x: inverse_letter(x), filter(lambda x: x.isalnum(), encoded.lower())))

def encode(decoded):
	message = ''.join(map(lambda x: inverse_letter(x), filter(lambda x: x.isalnum(), decoded.lower())))
	return ' '.join([message[i:i+5] for i in range(0, len(message), 5)])