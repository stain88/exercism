class RunLengthEncoding
  def self.encode input
    input.scan(/(.)(\1*)/).map { |m|
      m[1].length == 0 ? m[0] : "#{m[1].length+1}#{m[0]}"
    }.join
  end

  def self.decode input
    input.scan(/((\d*)(.))/).map { |m|
      m[1].empty? ? m[2] : "#{m[2]*m[1].to_i}"
    }.join
  end
end

module BookKeeping
  VERSION = 2
end