class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        if True:
            for i in range(1, n):
                if nums[i] > nums[i - 1]:
                    cnt += 1
                else:
                    precnt, cnt = cnt, 1
                ans = max(ans, min(precnt, cnt))
                ans = max(ans, cnt // 2)
        if True:
            return ans
