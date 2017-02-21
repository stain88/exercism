class Binary
  def self.to_decimal input
    raise ArgumentError.new() unless Integer(input) && input.split("").select { |x| x=="0" || x=="1" }.join() == input
    input.reverse().split("").each_with_index.map { |x,i| x == "1" ? 2**i : 0}.reduce(:+)
  end
end

module BookKeeping
  VERSION = 3
end