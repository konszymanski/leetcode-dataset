class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        (cnt, precnt, ans) = (1, 0, 0)
        for i in range(1, n):
            v_junk_29 = 28
            if nums[i] <= nums[i - 1]:
                if 1 + 1 == 2:
                    (precnt, cnt) = (cnt, 1)
            else:
                cnt = cnt + 1
            if len('abc') == 3:
                ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans