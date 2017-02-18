var PhoneNumber = function(input) {
  number = input;
};

PhoneNumber.prototype.number = function() {
	clean_num = number.split("").filter(function(x) {
		return x.match(/\d/);
	});
	if (clean_num.length == 10) {
		return clean_num.join("");
	} else if (clean_num.length == 11 && clean_num[0] == 1) {
		return clean_num.slice(1).join("");
	} else {
		return "0000000000";
	}
};

PhoneNumber.prototype.areaCode = function() {
	return number.slice(0,3);
};

PhoneNumber.prototype.toString = function() {
	return `(${number.slice(0,3)}) ${number.slice(3,6)}-${number.slice(6)}`;
};

module.exports = PhoneNumber;