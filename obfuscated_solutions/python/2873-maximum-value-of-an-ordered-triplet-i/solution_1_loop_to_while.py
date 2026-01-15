class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
            i += 1
        return res
