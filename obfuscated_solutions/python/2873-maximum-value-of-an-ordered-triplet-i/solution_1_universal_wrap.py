class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        res = 0
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        res = max(res, (nums[i] - nums[j]) * nums[k])
        if True:
            return res
