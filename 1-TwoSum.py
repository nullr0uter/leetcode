class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    dicts = {}
    for i in range(0, len(numbers)):
      if target - numbers[i] in dicts:
        return [dicts[target - numbers[i]], i]
      else:
        dicts[numbers[i]] = i
