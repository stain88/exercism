class BookKeeping
	VERSION = 3
end

class Pangram
	def self.pangram? phrase
		alphabet = ("a".."z").to_a
		phrase.downcase.split("").each do |letter|
			alphabet -= [letter]
		end
		alphabet.empty?
	end
end