class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    stripped = s.strip()
    result = stripped.split(" ")
    return len(result[-1])
