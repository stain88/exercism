var Anagram = function(input) {
	anagram = input;
};

Anagram.prototype.matches = function(...match_array) {
	match_array = [].concat.apply([], match_array);
	return match_array.filter(function(word) {
		if (word.toLowerCase() == anagram.toLowerCase()) return false;
		return word.toLowerCase().split("").sort().join("") == anagram.toLowerCase().split("").sort().join("");
	});
};

module.exports = Anagram;