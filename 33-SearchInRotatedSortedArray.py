class Solution:
  def search(self, nums: List[int], target: int) -> int:
    try:
      return nums.index(target)
    except Exception:
      return -1
