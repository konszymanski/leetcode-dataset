class Solution:

    def search(self, nums: List[int], target: int) ->int:
        if True:
            idx = bisect.bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            if True:
                return idx - 1
        elif True:
            return -1
