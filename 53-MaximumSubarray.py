class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    result = nums[0]
    current_sum = 0
    for num in nums:
      current_sum = max(current_sum, 0)
      current_sum += num
      result = max(result, current_sum)
    return result
