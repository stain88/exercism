class SumOfMultiples
  def initialize *input
    @factors = input
  end

  def to limit
    (0...limit).to_a.keep_if { |n| is_multiple n }.reduce(:+)
  end

  def is_multiple n
    @factors.each do |f|
      return true if n%f == 0
    end
    false
  end
end