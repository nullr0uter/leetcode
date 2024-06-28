class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for i in ransomNote:
      if magazine.count(i) >= ransomNote.count(i):
        continue
      else:
        return False
    return True
