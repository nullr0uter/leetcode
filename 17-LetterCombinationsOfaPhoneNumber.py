class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    d = {
      '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
    }
    res, curr = [], []

def backtrack(start):
  if start == len(digits):
    res.append(''.join(curr))
  else:
    for letter in d[digits[start]]:
      curr.append(letter)
      backtrack(start + 1)
      curr.pop()
if not digits:
  return []
  backtrack(0)
  return res
