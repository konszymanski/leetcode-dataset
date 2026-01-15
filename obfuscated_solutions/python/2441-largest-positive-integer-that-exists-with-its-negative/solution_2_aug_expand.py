class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if -nums[lo] == nums[hi]:
                return nums[hi]
            elif -nums[lo] > nums[hi]:
                lo = lo + 1
            else:
                hi = hi - 1
        return -1
