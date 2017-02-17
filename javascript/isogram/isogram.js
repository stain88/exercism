var Isogram = function(input) {
	word = input;
};

Isogram.prototype.isIsogram = function() {
	return word.toLowerCase().split("").sort().join("").match(/([^-\s])\1/) === null;
};

module.exports = Isogram;