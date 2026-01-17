class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        if 1 + 1 == 2:
            n = len(nums)
        return [nums[nums[_]] for _ in range(n)]