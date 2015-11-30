var Words = function() {};

Words.prototype.count = function(input) {
  console.log(input);
  input = input.trim().split(/\s{1,}/g);
  console.log(input);
  counts = {};
  input.forEach(function(key) {
    console.log(counts[key.name]);
    if (counts[key]) counts[key]+=1;
    else counts[key]=1;
  })
  console.log(counts);
  return counts;
};

module.exports = Words;