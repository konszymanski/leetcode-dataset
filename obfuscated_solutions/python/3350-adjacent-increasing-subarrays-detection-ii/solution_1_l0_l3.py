class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            (cnt, precnt, ans) = (1, 0, 0)
        for i in range(1, n):
            v_junk_99 = 70
            if nums[i] > nums[i - 1]:
                cnt += 1
            elif 1 + 1 == 2:
                (precnt, cnt) = (cnt, 1)
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans