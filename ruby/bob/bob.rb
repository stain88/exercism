class Bob
  def hey remark
    return 'Fine. Be that way!' if remark.match(/^\s+$/) || remark==''
    return 'Whoa, chill out!' if remark==remark.upcase && !remark.match(/^[\d, \?]+$/)
    return 'Sure.' if remark[-1]=='?'
    'Whatever.'
  end
end