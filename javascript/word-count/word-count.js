var Words = function() {};

Words.prototype.count = function(input) {
  input = input.trim().split(/\s{1,}/g);
  var counts = {};
  input.forEach(function(key) {
    if (counts[key]) counts[key]++;
    else counts[String(key)]=1;
  })
  return counts;
};

module.exports = Words;