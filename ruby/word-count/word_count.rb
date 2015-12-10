class Phrase
  VERSION = 1
  def initialize x
    @phrase = x
  end

  def word_count
    count = {}
    @phrase.gsub(/[^\w']+/,' ').gsub(/'(\w+)'/,'\1').split(/\s/).each do |word|
      if count[word.downcase] then count[word.downcase]+=1
      else count[word.downcase] = 1 end
    end
    count
  end
end