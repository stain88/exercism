class Robot
  @name = ""
  def initialize
  end

  def name
    unless @name
      a=(0...2).map{('A'..'Z').to_a[rand(26)]}.join
      b=(0...3).map{(0..9).to_a[rand(10)]}.join
      @name = a+b
    end
    @name
  end

  def reset
    a=(0...2).map{('A'..'Z').to_a[rand(26)]}.join
    b=(0...3).map{(0..9).to_a[rand(10)]}.join
    @name = a+b
  end
end