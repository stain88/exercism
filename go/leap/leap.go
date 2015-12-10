package leap

const TestVersion = 1

func IsLeapYear(a int) bool {
  if a%400==0 {
    return true
  } else if a%100==0 {
    return false
  }
  return a%4==0
}
