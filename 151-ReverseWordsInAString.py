class Solution:
  def reverseWords(self, s: str) -> str:
    tmp: List[int] = []
    tmp = s.split()
    result: str = ""
    for i in range(len(tmp)):
      i += 1
      result = result + tmp[-1] + " "
    return result.strip()
