var DnaTranscriber = function() {};

DnaTranscriber.prototype.toRna = function(strand) {
  var dnaToRna = {"C":"G","G":"C","A":"U","T":"A"};
  var transcribed = "";
  for (var i=0;i<strand.length;i++) {
    transcribed+=dnaToRna[strand.charAt(i)];
  }
  return transcribed;
};

DnaTranscriber.prototype.toDna = function(strand) {
  var rnaToDna = {"C":"G","G":"C","U":"A","A":"T"};
  var transcribed = "";
  for (var i=0;i<strand.length;i++) {
    transcribed+=rnaToDna[strand.charAt(i)];
  }
  return transcribed;
};

module.exports = DnaTranscriber;