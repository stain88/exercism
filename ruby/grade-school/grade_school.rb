class School
  def initialize
    @schools = []
  end

  def students grade
    @schools.select {|school| school[:grade] == grade}.empty? ? [] : @schools.select {|school| school[:grade] == grade}[0][:students]
  end

  def add student, grade
    year = @schools.select {|school| school[:grade] == grade}
    if year.empty?
      @schools.push({:grade => grade, :students => [student]})
    else
      year[0][:students].push student
      year[0][:students].sort!
    end
  end

  def students_by_grade
    @schools.sort_by { |s| s[:grade]}
  end
end

module BookKeeping
  VERSION = 3
end