class Solution:
  def addBinary(self, a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    result = x + y
    result = str(bin(result))
    index = result.find('b')
    return result[index + 1:]
