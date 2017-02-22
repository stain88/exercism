module Accumulate
  def accumulate
    self.map { |item| Proc.new.call item }
  end
end

module BookKeeping
  VERSION = 1
end

Array.include Accumulate