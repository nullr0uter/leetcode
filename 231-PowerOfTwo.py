class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return True if bin(n)[2:].rstrip('0') == '1' else False
