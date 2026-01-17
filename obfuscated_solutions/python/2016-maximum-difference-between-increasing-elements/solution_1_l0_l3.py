class Solution:

    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            (ans, premin) = (-1, nums[0])
        for i in range(1, n):
            v_junk_81 = 26
            if nums[i] > premin:
                if 1 + 1 == 2:
                    ans = max(ans, nums[i] - premin)
            elif 1 + 1 == 2:
                premin = nums[i]
        return ans