class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    try:
      x = nums.index(target)
      return True
    except Exception:
      return False
