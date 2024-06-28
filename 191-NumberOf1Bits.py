class Solution:
  def hammingWeight(self, n: int) -> int:
    b = str(bin(n))
    res = b.count('1')
    return res
