var FoodChain = function() {
	special_line = [
		"I know an old lady who swallowed a fly.\n",
		"I know an old lady who swallowed a spider.\nIt wriggled and jiggled and tickled inside her.\n",
		"I know an old lady who swallowed a bird.\nHow absurd to swallow a bird!\n",
		"I know an old lady who swallowed a cat.\nImagine that, to swallow a cat!\n",
		"I know an old lady who swallowed a dog.\nWhat a hog, to swallow a dog!\n",
		"I know an old lady who swallowed a goat.\nJust opened her throat and swallowed a goat!\n",
		"I know an old lady who swallowed a cow.\nI don't know how she swallowed a cow!\n"
	];
	lines = [
		"She swallowed the cow to catch the goat.",
		"She swallowed the goat to catch the dog.",
		"She swallowed the dog to catch the cat.",
		"She swallowed the cat to catch the bird.",
		"She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
		"She swallowed the spider to catch the fly.",
		"I don't know why she swallowed the fly. Perhaps she'll die.\n"
	];
};

FoodChain.prototype.verse = function(verse_num) {
	if (verse_num == 8) {
		return "I know an old lady who swallowed a horse.\nShe's dead, of course!\n";
	} else {
		return special_line[verse_num-1].toString() + lines.slice(lines.length - verse_num).join("\n").toString();
	}
};

FoodChain.prototype.verses = function(start_verse, end_verse) {
	sing = "";
	for (var i = start_verse; i <= end_verse; i++) {
		sing += this.verse(i) + "\n";
	}
	return sing;
};

module.exports = FoodChain;