class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[0:m+n] = sorted(nums1[:m] + nums2[:n])
