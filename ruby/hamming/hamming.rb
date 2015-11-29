class Hamming
  VERSION = 1
  def self.compute first_string, second_string
    if first_string.length != second_string.length
      raise ArgumentError
    else
      count = 0
      for i in 0...first_string.length
        if first_string[i] != second_string[i]
          count += 1
        end
      end
    end
    count
  end
end