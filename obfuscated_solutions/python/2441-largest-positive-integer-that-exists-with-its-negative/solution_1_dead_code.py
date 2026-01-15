class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        ans = -1
        udaxi = 32 * 2
        for i in nums:
            for j in nums:
                if i == -j:
                    ans = max(ans, abs(i))
        return ans
