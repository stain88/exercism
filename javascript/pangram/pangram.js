var Pangram = function(input) {
	string = input.toLowerCase();
};

Pangram.prototype.isPangram = function() {
	var alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
	return alphabet.filter(function(i) { return string.indexOf(i) < 0;}).length === 0;
};

module.exports = Pangram;