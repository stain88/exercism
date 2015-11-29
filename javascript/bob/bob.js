//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
//
// YOUR CODE GOES HERE
//
  console.log("\""+input+"\"");
  if (input.charAt(input.length-1)==='?') {
    if (/^[A-Z\s]+$/.test(input.substring(0,input.length-1))) return "Whoa, chill out!";
    return "Sure.";
  }
  if (/^[\d,\s]+$/.test(input)) return "Whatever.";
  if (/^[A-Z\s,\d\%\^\*\@\#\$\(!\u00c4\u00dc]+!?$/.test(input)) return "Whoa, chill out!";
  if (/^\s*$/.test(input)) return "Fine. Be that way!";
  return "Whatever.";
};

module.exports = Bob;
