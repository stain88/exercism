module BookKeeping
	VERSION = 1
end

class Sieve
	def initialize n
		@limit = n
		@prime_array = []
	end

	def primes
		(1..@limit).each do |num|
			is_prime? num
		end
		@prime_array
	end

	def is_prime? num
		return false if num == 1
		unless @prime_array.empty?
			@prime_array.each do |prime|
				return false if num % prime == 0
			end
		end
		@prime_array.push num
	end
end