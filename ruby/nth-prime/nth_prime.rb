class Prime
  def self.nth(x)
    if x<1 
      raise ArgumentError
    end

    primes = 0
    i = 1
    while primes < x
      i += 1
      primes += 1 if self.isPrime?(i)
    end
    i
  end

  def self.isPrime?(n)
    return false if n==1 
    return true if n==2 
    (2..Math.sqrt(n).ceil).each do |i|
      return false if n%i==0
    end
    return true
  end
end