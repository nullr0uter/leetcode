class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    result: List[int] = []
    left: int = 0
    right: int = len(numbers) - 1
    while left < right:
      tmp: int = numbers[left] + numbers[right]
      if tmp == target:
        result.append(left + 1)
        result.append(right + 1)
        break
      elif tmp < target:
        left += 1
      elif tmp > target:
        right -= 1
      else:
        return []
    return result
