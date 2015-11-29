var Gigasecond = function(input) {
  time = input;
};

Gigasecond.prototype.date = function() {
  return new Date(time.getTime()+Math.pow(10,12));
};

module.exports = Gigasecond;