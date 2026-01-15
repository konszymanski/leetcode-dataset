class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        while True:
            if not lo < hi:
                break
            if -nums[lo] == nums[hi]:
                return nums[hi]
            elif -nums[lo] > nums[hi]:
                lo += 1
            else:
                hi -= 1
        return -1
