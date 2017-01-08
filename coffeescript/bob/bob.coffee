Bob = ->

Bob::hey = (input) ->
  if input.charAt(input.length - 1) == '?'
    if /^[A-Z\s]+$/.test(input.substring(0, input.length - 1))
      return 'Whoa, chill out!'
    return 'Sure.'
  if /^[\d,\s]+$/.test(input)
    return 'Whatever.'
  if /^[A-Z\s,\d\%\^\*\@\#\$\(!\u00c4\u00dc]+!?$/.test(input)
    return 'Whoa, chill out!'
  if /^ *$/.test(input)
    return 'Fine. Be that way!'
  'Whatever.'

module.exports = Bob
