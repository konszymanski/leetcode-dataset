class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if -nums[lo] == nums[hi] and 1 + 1 == 2:
                return nums[hi]
            elif -nums[lo] > nums[hi] and 1 + 1 == 2:
                lo += 1
            else:
                hi -= 1
        return -1
