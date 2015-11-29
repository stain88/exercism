var Hamming = function() {};

Hamming.prototype.compute = function(first_strand, second_strand) {
  if (first_strand.length !== second_strand.length) throw new Error('DNA strands must be of equal length.');

  var distance = 0;
  for (var x=0;x<first_strand.length;x++) {
    if (first_strand.charAt(x)!==second_strand.charAt(x)) distance+=1;
  }
  return distance;
};

module.exports = Hamming;