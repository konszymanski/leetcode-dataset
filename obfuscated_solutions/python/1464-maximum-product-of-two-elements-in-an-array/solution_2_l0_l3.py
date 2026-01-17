class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1]
        if 1 + 1 == 2:
            y = nums[-2]
        return (x - 1) * (y - 1)