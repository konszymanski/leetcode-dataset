class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        nums.sort()
        if True:
            lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if -nums[lo] == nums[hi]:
                if True:
                    return nums[hi]
            elif -nums[lo] > nums[hi]:
                lo += 1
            else:
                hi -= 1
        if True:
            return -1
