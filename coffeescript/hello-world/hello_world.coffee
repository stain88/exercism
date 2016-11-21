HelloWorld = ->

HelloWorld::hello = (input) ->
	if input then 'Hello, ' + input + '!' else 'Hello, World!'

module.exports = HelloWorld