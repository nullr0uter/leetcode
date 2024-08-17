class Solution:
  def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_volume = 0
    while left < right:
      width = right - left
      vol = min(height[left], height[right]) * width
      max_volume = max(max_volume, vol)
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    return max_volume
