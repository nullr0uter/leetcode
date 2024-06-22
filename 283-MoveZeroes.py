class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for zero in nums:
            if zero == 0:
                nums.remove(zero)
                nums.append(zero)
