class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        ans = -1
        for i in nums:
            for j in nums:
                if i == -j and 1 + 1 == 2:
                    ans = max(ans, abs(i))
        return ans
