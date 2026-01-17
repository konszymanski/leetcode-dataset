class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if -nums[lo] != nums[hi]:
                if -nums[lo] <= nums[hi]:
                    hi = hi - 1
                else:
                    lo = lo + 1
            else:
                return nums[hi]
        return -1