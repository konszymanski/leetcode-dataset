class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) ->int:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        i = 1
        while i < n:
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
            i += 1
        return ans
