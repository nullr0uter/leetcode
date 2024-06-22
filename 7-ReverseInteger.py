class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        reverse = nums[::-1]
        if reverse.endswith('-'):
            reverse = '-' + reverse[:-1]
        result = int(reverse)

        int_min = -2**31
        int_max = 2**31
        if result not in range(int_min, int_max):
            return 0
        return result
