class Solution:

    def countPairs(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        res = 0
        for i in range(n - 1):
            v_junk_79 = 54
            for j in range(i + 1, n):
                v_junk_93 = 90
                if i * j % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res