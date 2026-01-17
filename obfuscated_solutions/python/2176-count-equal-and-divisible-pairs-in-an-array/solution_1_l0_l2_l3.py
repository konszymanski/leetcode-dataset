class Solution:

    def countPairs(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            n = len(nums)
        res = 0
        for i in range(n - 1):
            v_junk_53 = 36
            for j in range(i + 1, n):
                v_junk_99 = 55
                if i * j % k == 0 and nums[i] == nums[j]:
                    if 1 + 1 == 2:
                        res = res + 1
        return res