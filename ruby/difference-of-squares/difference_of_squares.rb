class Squares
  def initialize x
    @max = x
  end

  def square_of_sums
    total = 0
    for i in 1..@max
      total += i
    end
    total**2
  end

  def sum_of_squares
    total = 0
    for i in 1..@max
      total += i**2
    end
    total
  end

  def difference
    square_of_sums - sum_of_squares
  end
end