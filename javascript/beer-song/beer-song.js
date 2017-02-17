var BeerSong = function() {

};

BeerSong.prototype.verse = function(line) {
	if (line > 2) {
		return `${line} bottles of beer on the wall, ${line} bottles of beer.\nTake one down and pass it around, ${line - 1} bottles of beer on the wall.\n`;
	} else if (line == 2) {
		return `${line} bottles of beer on the wall, ${line} bottles of beer.\nTake one down and pass it around, ${line - 1} bottle of beer on the wall.\n`;
	} else if (line == 1) {
		return `${line} bottle of beer on the wall, ${line} bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n`;
	} else {
		return 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n';
	}
};

BeerSong.prototype.sing = function(start_verse, end_verse = 0) {
	song = []
	for (var i = start_verse; i != end_verse - 1; i--) {
		song.push(this.verse(i));
	}
	return song.join("\n")
};

module.exports = BeerSong;