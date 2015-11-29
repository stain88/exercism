class Complement
  VERSION = 2
  def self.of_dna strand
    r_strand = ""
    for i in 0...strand.length
      case strand[i]
      when 'C' then r_strand<<'G'
      when 'G' then r_strand<<'C'
      when 'T' then r_strand<<'A'
      when 'A' then r_strand<<'U'
      else raise ArgumentError
      end
    end
    r_strand
  end
  def self.of_rna strand
    d_strand = ""
    for i in 0...strand.length
      case strand[i]
      when 'C' then d_strand<<'G'
      when 'G' then d_strand<<'C'
      when 'U' then d_strand<<'A'
      when 'A' then d_strand<<'T'
      else raise ArgumentError
      end
    end
    d_strand
  end
end