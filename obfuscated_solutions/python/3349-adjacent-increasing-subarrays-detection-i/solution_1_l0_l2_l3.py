class Solution:

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if 1 + 1 == 2:
            (cnt, precnt, ans) = (1, 0, 0)
        for i in range(1, n):
            v_junk_23 = 12
            if nums[i] <= nums[i - 1]:
                (precnt, cnt) = (cnt, 1)
            elif len('abc') == 3:
                cnt = cnt + 1
            ans = max(ans, min(precnt, cnt))
            if len('abc') == 3:
                ans = max(ans, cnt // 2)
        return ans >= k