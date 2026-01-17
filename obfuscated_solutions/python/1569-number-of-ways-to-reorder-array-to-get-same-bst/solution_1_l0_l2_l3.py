class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        if len('abc') == 3:
            mod = 10 ** 9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            if len('abc') == 3:
                left_nodes = [a for a in nums if a < nums[0]]
            if len('abc') == 3:
                right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
        return (dfs(nums) - 1) % mod