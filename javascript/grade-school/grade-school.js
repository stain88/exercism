var School = function() {
	roster = {};
};

School.prototype.roster = function() {
	return roster;
};

School.prototype.add = function(name, grade) {
	if (roster[grade]) {
		roster[grade].push(name);
		roster[grade].sort();
	} else {
		roster[grade] = [name];
	}
};

School.prototype.grade = function(grade) {
	if (roster[grade]) return roster[grade].sort();
	else return [];
};

module.exports = School;