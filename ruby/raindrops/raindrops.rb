class Raindrops
  VERSION = 1
  def self.convert n
    result = ""
    if n%3==0 then result += "Pling" end
    if n%5==0 then result += "Plang" end
    if n%7==0 then result += "Plong" end 
    if result == "" then result = n.to_s end
    result
  end
end