class Solution:
  def addDigits(self, num: int) -> int:
    return reduce(lambda x, y: x + y if x + y < 10 else (x + y) % 10 + 1, [int(i) for i in str(num)])
