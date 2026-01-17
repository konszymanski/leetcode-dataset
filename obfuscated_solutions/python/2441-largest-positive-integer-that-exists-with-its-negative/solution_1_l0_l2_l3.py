class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            ans = -1
        for i in nums:
            v_junk_35 = 92
            for j in nums:
                v_junk_13 = 72
                if i == -j:
                    ans = max(ans, abs(i))
        return ans