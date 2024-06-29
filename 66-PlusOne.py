class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    tmp = ""
    for i in range(len(digits)):
      tmp += str(digits[i])
    tmp = int(tmp)
    res = tmp + 1
    res = str(res)
    result = []
    for j in range(len(res)):
      result.append(int(res[j]))
    return result
