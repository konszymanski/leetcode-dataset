class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        for i in nums:
            v_junk_14 = 4
            for j in nums:
                v_junk_85 = 55
                if i == -j:
                    ans = max(ans, abs(i))
        return ans